import reflex as rx

# Application
from churuchuru.apps.counter import counter
from churuchuru.apps.imagetopdf import imagetopdf
from churuchuru.apps.notetaking import notetaking


# Theme
from churuchuru.layout import layout, app_card, Color
from churuchuru.components.colors import COLORS


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
                # Cards Section
                rx.flex(
                    app_card("Counter", "Add, subtract, or reset a counter.", "/counter", theme),
                    app_card("Image to PDF", "Convert any image to a PDF.", "/imagetopdf", theme),
                    app_card("Note Taking", "Write any notes and convert to any format.", "/notetaking", theme),
                    spacing="4",
                    justify="center",
                    align="center",
                    flex_wrap="wrap",
                    width="100%",
                    animate="slideUp",  # Smooth slide-up animation
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
