import reflex as rx
from churuchuru.layout import layout, Color
from churuchuru.components.colors import COLORS
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document
from PIL import Image, ImageDraw, ImageFont
import logging
import time
import hashlib

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Generic function to generate a unique ID
def generate_unique_id() -> str:
    """Generate a unique ID using the current timestamp and MD5 hash."""
    timestamp = str(time.time()).encode('utf-8')
    return hashlib.md5(timestamp).hexdigest()[:8]  # Truncate to 8 characters for simplicity

class State(rx.State):
    """The app state."""
    text: str = ""  # Store the note text
    download_filename: str = ""  # Store the filename for download

    @rx.event
    def clear_note(self):
        """Clear the note from the state."""
        self.text = ""
        self.download_filename = ""  # Clear the download filename

    @rx.event
    def export_note(self, format: str):
        """Export the note in the specified format."""
        if not self.text:
            logger.warning("No note text to export.")
            return

        try:
            unique_id = generate_unique_id()  # Use the generic function to generate a unique ID
            filename = f"note_{unique_id}.{format}"
            file_path = rx.get_upload_dir() / filename

            if format == "txt":
                self._export_txt(file_path)
            elif format == "pdf":
                self._export_pdf(file_path)
            elif format == "docx":
                self._export_docx(file_path)
            elif format == "png":
                self._export_png(file_path)
            elif format == "md":
                self._export_md(file_path)
            else:
                logger.error(f"Unsupported export format: {format}")
                return

            logger.info(f"Note exported successfully as {filename}")
            self.download_filename = filename  # Set the filename for download
        except Exception as e:
            logger.error(f"Error exporting note: {e}")

    def _export_txt(self, file_path):
        """Export the note as a TXT file."""
        with file_path.open("w") as file_object:
            file_object.write(self.text)

    def _export_pdf(self, file_path):
        """Export the note as a PDF file using ReportLab."""
        c = canvas.Canvas(str(file_path), pagesize=letter)
        width, height = letter
        text = c.beginText(40, height - 40)
        text.setFont("Helvetica", 12)
        for line in self.text.splitlines():
            text.textLine(line)
        c.drawText(text)
        c.save()

    def _export_docx(self, file_path):
        """Export the note as a Word document using python-docx."""
        doc = Document()
        doc.add_paragraph(self.text)
        doc.save(file_path)

    def _export_png(self, file_path):
        """Export the note as a PNG image using Pillow."""
        img = Image.new('RGB', (800, 600), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        d.text((10, 10), self.text, fill=(0, 0, 0), font=font)
        img.save(file_path)

    def _export_md(self, file_path):
        """Export the note as a Markdown file."""
        with file_path.open("w") as file_object:
            file_object.write(self.text)

def notetaking() -> rx.Component:
    theme = rx.cond(
        Color.is_dark_mode,
        COLORS["dark"],
        COLORS["light"],
    )

    return layout(
        rx.vstack(
            rx.heading("Note Taking", size="4", color=theme["primary"]),

            rx.text_area(
                placeholder="Take your notes here...",
                value=State.text,
                on_change=State.set_text,
                bg=theme["card_bg"],
                color=theme["text"],
                border=f"1px solid {theme['border']}",
                size="2",
                height="200px",
                width="100%",
            ),

            rx.hstack(
                # Show Export and Clear buttons only if there is text
                rx.cond(
                    State.text != "",
                    rx.hstack(
                        rx.menu.root(
                            rx.menu.trigger(
                                rx.button("Export", 
                                    bg=theme["card_bg"],
                                    color=theme["text"], 
                                    border=f"1px solid {theme['border']}",
                                    _hover={"bg": theme["hover"]},
                                    size="2"
                                ),
                            ),
                            rx.menu.content(
                                rx.menu.item("Export as TXT", on_click=lambda: State.export_note("txt")),
                                rx.menu.item("Export as PDF", on_click=lambda: State.export_note("pdf")),
                                rx.menu.item("Export as Word", on_click=lambda: State.export_note("docx")),
                                rx.menu.item("Export as Image", on_click=lambda: State.export_note("png")),
                                rx.menu.item("Export as Markdown", on_click=lambda: State.export_note("md")),
                            ),
                        ),
                        rx.button(
                            "Clear Note",
                            on_click=State.clear_note,
                            bg=theme["card_bg"],
                            color=theme["text"],
                            border=f"1px solid {theme['border']}",
                            _hover={"bg": theme["hover"]},
                            size="2",
                        ),
                        spacing="4",
                    ),
                ),
                spacing="4",
                wrap="wrap",  # Enable wrapping
                width="100%",  # Full width container
                justify="center",  # Center buttons
            ),

            # Download button (only shown when a file is ready to download)
            rx.cond(
                State.download_filename != "",
                rx.button(
                    "Download File",
                    bg=theme["card_bg"],
                    color=theme["text"],
                    border=f"1px solid {theme['border']}",
                    _hover={"bg": theme["hover"]},
                    size="2",
                    on_click=rx.download(
                        url=rx.get_upload_url(State.download_filename),
                        filename=State.download_filename
                    ),
                ),
            ),

            padding="5em",
            spacing="6",
            align="center",
            bg=theme["background"],
            min_h="100vh",
        ),
        theme=theme
    )