import reflex as rx

# Logics
from PIL import Image
import os
import hashlib
import time

# Theme
from churuchuru.layout import layout, Color
from churuchuru.components.colors import COLORS

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

                # Remove metadata, instead of using exiftool
                # Solves issues of combining into PDF where you get replica copies of images
                img.save(img_path, "JPEG", quality=100)
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
    # Use rx.cond to dynamically select the theme
    theme = rx.cond(
        Color.is_dark_mode,
        COLORS["dark"],
        COLORS["light"],
    )
    
    return layout(
        rx.vstack(
            rx.heading("Image to PDF", size="4", color=theme["primary"]),  # Apply theme color to heading
            
            rx.upload(
                rx.vstack(
                    rx.button(
                        "Select Images",
                        bg=theme["card_bg"],  # Apply theme background to button
                        color=theme["text"],  # Apply theme text color to button
                        border=f"1px solid {theme['border']}",  # Apply theme border to button
                        _hover={"bg": theme["hover"]},  # Apply theme hover effect
                        size="2",  # Numeric size
                    ),
                    rx.text(
                        "Drag and drop image files here or click to select",
                        color=theme["text"],  # Apply theme text color
                        font_size="sm",
                    ),
                    align="center",
                    spacing="2",
                ),
                id="upload_1",
                border="2px dashed",
                border_color=theme["border"],  # Apply theme border color
                padding="5em",
                bg=theme["card_bg"],  # Apply theme background to upload area
                rounded="lg",
            ),
            rx.hstack(
                rx.foreach(
                    rx.selected_files("upload_1"), 
                    lambda file: rx.text(file, color=theme["text"], font_size="sm")  # Apply theme text color
                ),
                spacing="2",
            ),
            rx.hstack(
                rx.button(
                    "Upload",
                    on_click=State.handle_upload(rx.upload_files(upload_id="upload_1")),
                    bg=theme["card_bg"],  # Apply theme background to button
                    color=theme["text"],  # Apply theme text color to button
                    border=f"1px solid {theme['border']}",  # Apply theme border to button
                    _hover={"bg": theme["hover"]},  # Apply theme hover effect
                    size="2",  # Numeric size
                ),
                rx.button(
                    "Clear",
                    on_click=[
                        State.clear_files,
                        rx.clear_selected_files("upload_1")
                    ],
                    bg=theme["card_bg"],  # Apply theme background to button
                    color=theme["text"],  # Apply theme text color to button
                    border=f"1px solid {theme['border']}",  # Apply theme border to button
                    _hover={"bg": theme["hover"]},  # Apply theme hover effect
                    size="2",  # Numeric size
                ),
                rx.button(
                    "Convert to PDF",
                    on_click=State.convert_to_pdf,
                    bg=theme["card_bg"],  # Apply theme background to button
                    color=theme["text"],  # Apply theme text color to button
                    border=f"1px solid {theme['border']}",  # Apply theme border to button
                    _hover={"bg": theme["hover"]},  # Apply theme hover effect
                    size="2",  # Numeric size
                ),
                spacing="4",
            ),
            
            # Download button - only shown when PDF is available
            rx.cond(
                State.pdf_file != "",
                rx.link(
                    rx.button(
                        "Download PDF",
                        bg=theme["card_bg"],  # Apply theme background to button
                        color=theme["text"],  # Apply theme text color to button
                        border=f"1px solid {theme['border']}",  # Apply theme border to button
                        _hover={"bg": theme["hover"]},  # Apply theme hover effect
                        size="2",  # Numeric size
                    ),
                    href=rx.get_upload_url(State.pdf_file),
                    is_external=True,
                    download=True,
                ),
            ),
            
            rx.foreach(
                State.img,
                lambda img: rx.image(
                    src=rx.get_upload_url(img),
                    border="1px solid",
                    border_color=theme["border"],  # Apply theme border color
                    rounded="lg",
                    shadow="sm",
                ),
            ),

            padding="5em",
            spacing="6",
            align="center",
            bg=theme["background"],  # Apply theme background to the page
            min_h="100vh",
        ),
        theme=theme
    )