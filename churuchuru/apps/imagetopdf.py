import reflex as rx
from PIL import Image
import os
import hashlib
import time
from churuchuru.layout import layout

class State(rx.State):
    """The app state."""
    img: list[str] = []  # Store uploaded images
    pdf_file: str = ""  # Store the generated PDF filename
    upload_hash: str = ""  # Store the unique upload hash
    
    def generate_upload_hash(self) -> str:
        """Generate a unique hash for the upload session."""
        timestamp = str(time.time()).encode('utf-8')
        return hashlib.md5(timestamp).hexdigest()[:8]

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s)."""
        # Generate new hash if this is the first upload
        if not self.upload_hash:
            self.upload_hash = self.generate_upload_hash()
            
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var
            self.img.append(file.filename)

    @rx.event
    def clear_files(self):
        """Handle the deletion of file(s)."""
        # Get the upload directory path
        file_path = rx.get_upload_dir()
        
        # Delete each file in the img list
        for filename in self.img:
            try:
                os.remove(file_path / filename)
            except Exception as e:
                print(f"Error deleting {filename}: {e}")
        
        # Delete PDF if it exists
        if self.pdf_file:
            try:
                os.remove(file_path / self.pdf_file)
            except Exception as e:
                print(f"Error deleting PDF {self.pdf_file}: {e}")
        
        # Clear the state
        self.img = []
        self.pdf_file = ""
        self.upload_hash = ""
    
    @rx.event
    async def convert_to_pdf(self):
        """
        Convert uploaded images to a single PDF file.
        Returns the path to the generated PDF file.
        """
        if not self.img:
            return None
        
        try:
            # Get the upload directory path
            upload_dir = rx.get_upload_dir()
            
            # Open all images
            images = []
            first_image = None
            
            for img_name in self.img:
                img_path = upload_dir / img_name
                img = Image.open(img_path)
                
                # Convert to RGB if necessary
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                if first_image is None:
                    first_image = img
                else:
                    images.append(img)
            
            if first_image:
                # Generate PDF filename with hash
                self.pdf_file = f"converted_images_{self.upload_hash}.pdf"
                pdf_path = upload_dir / self.pdf_file
                
                # Save as PDF
                first_image.save(
                    pdf_path,
                    "PDF",
                    save_all=True,
                    append_images=images,
                    resolution=100.0
                )
                
        except Exception as e:
            print(f"Error converting to PDF: {e}")
            self.pdf_file = ""

def imagetopdf() -> rx.Component:
    return layout(
        rx.vstack(
            rx.heading("Image to PDF Converter"),
            
            rx.upload(
                rx.vstack(
                    rx.button(
                        "Select Images",
                        color_scheme="blue",
                    ),
                    rx.text(
                        "Drag and drop image files here or click to select"
                    ),
                ),
                id="upload_1",
                border="1px dotted rgb(107,99,246)",
                padding="5em",
            ),
            rx.hstack(
                rx.foreach(
                    rx.selected_files("upload_1"), 
                    rx.text
                )
            ),
            rx.hstack(
                rx.button(
                    "Upload",
                    on_click=State.handle_upload(
                        rx.upload_files(upload_id="upload_1")
                    ),
                ),
                rx.button(
                    "Clear",
                    on_click=[
                        State.clear_files,
                        rx.clear_selected_files("upload_1")
                    ],
                ),
                rx.button(
                    "Convert to PDF",
                    on_click=[
                        State.convert_to_pdf,
                    ],
                ),
            ),
            
            # Download button - only shown when PDF is available
            rx.cond(
                State.pdf_file != "",
                rx.link(
                    rx.button(
                        "Download PDF",
                        color_scheme="green",
                    ),
                    href=rx.get_upload_url(State.pdf_file),
                    is_external=True,
                    download=True,
                ),
            ),
            
            rx.foreach(
                State.img,
                lambda img: rx.image(
                    src=rx.get_upload_url(img)
                ),
            ),

            padding="5em",
            spacing="4",
            align='center',
        )
    )