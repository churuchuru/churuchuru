import reflex as rx

# Application
from churuchuru.apps.counter import counter
from churuchuru.apps.imagetopdf import imagetopdf
from churuchuru.apps.notetaking import notetaking

# Theme
from churuchuru.layout import layout, app_card, Color
from churuchuru.components.colors import COLORS

# Cleanup functionality
from churuchuru.components.cleanup import start_cleanup_scheduler

# Define the upload directory and retention period
UPLOAD_DIR = "./uploaded_files"
RETENTION_PERIOD_SECONDS = 60 * 3 # 60 seconds

# Start the cleanup scheduler when the application starts
start_cleanup_scheduler(UPLOAD_DIR, RETENTION_PERIOD_SECONDS)

# Main page with shadcn/ui-inspired design
def index():
    # Use rx.cond to dynamically select the theme
    theme = rx.cond(
        Color.is_dark_mode,
        COLORS["dark"],
        COLORS["light"],
    )

    return layout(
        rx.center(
            rx.vstack(
                # Hero Section
                rx.box(
                    rx.heading("churu churu", size="9", color=theme["primary"]),
                    rx.text("useful tools without the bs", size="5", color=theme["text"]),
                    text_align="center",
                    padding_bottom="2em",
                    animate="fadeIn",  # Smooth fade-in animation
                ),
                # Improved cards section with grid layout and better responsiveness
                rx.grid(
                    app_card("Counter", "Add, subtract, or reset a counter.", "/counter", theme),
                    app_card("Image to PDF", "Convert any image to a PDF.", "/imagetopdf", theme),
                    app_card("Note Taking", "Write any notes and convert to any format.", "/notetaking", theme),
                    template_columns={
                        "base": "1fr",  # Mobile: 1 card per row
                        "sm": "repeat(2, 1fr)",  # Tablet: 2 cards per row
                        "lg": "repeat(3, 1fr)",  # Desktop: 3 cards per row
                        "xl": "repeat(4, 1fr)",  # Large screens: 4 cards per row
                    },
                    gap="6",  # Increased gap for better spacing
                    padding="2em",
                    width="100%",
                    max_width="1200px",
                    margin="0 auto",
                    animate="fadeIn 0.5s ease-in-out",
                ),
                spacing="6",
                align="center",
                width="100%",
                max_width="1200px",
                padding="2em",
            ),
            height="100vh",
        ),
        theme=theme
    )

# Define application
app = rx.App()

# Add pages
app.add_page(index)
app.add_page(counter)
app.add_page(imagetopdf)
app.add_page(notetaking)