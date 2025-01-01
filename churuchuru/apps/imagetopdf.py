import reflex as rx
from PIL import Image
import os
from churuchuru.layout import layout

class State(rx.State):
    """The app state."""
    img: list[str] = []  # Store uploaded images
    
    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """
        Handle the upload of file(s).
        """
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
        """
        Handle the deletion of file(s).
        """
        # Get the upload directory path
        file_path = rx.get_upload_dir()
        
        # Delete each file in the img list
        for filename in self.img:
            try:
                os.remove(file_path / filename)
            except Exception as e:
                print(f"Error deleting {filename}: {e}")
                
        # Clear the img list
        self.img = []
    
    def convert_to_pdf(self):
        # Convert logic would go here
        pass

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