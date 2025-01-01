import reflex as rx
from churuchuru.apps.counter import counter
from churuchuru.apps.imagetopdf import imagetopdf
from churuchuru.layout import layout

# Define a theme with light and dark mode colors
MODERN_THEME = {
    "light": {
        "primary": "#6D28D9",  # Purple
        "secondary": "#1E40AF",  # Blue
        "background": "#F9FAFB",  # Light gray
        "text": "#1F2937",  # Dark gray
        "card_bg": "#FFFFFF",  # White
    },
    "dark": {
        "primary": "#8B5CF6",  # Lighter Purple
        "secondary": "#3B82F6",  # Lighter Blue
        "background": "#1F2937",  # Dark gray
        "text": "#F9FAFB",  # Light gray
        "card_bg": "#374151",  # Darker gray
    }
}

# Define the app state
class State(rx.State):
    is_dark_mode: bool = True  # Default to dark mode

    def toggle_theme(self):
        """Toggle between light and dark mode."""
        self.is_dark_mode = not self.is_dark_mode

# Theme toggle button
def theme_toggle():
    return rx.button(
        rx.cond(State.is_dark_mode, rx.icon(tag="moon"), rx.icon(tag="sun")),
        on_click=State.toggle_theme,
        position="fixed",
        bottom="1em",
        right="1em",
        z_index="999",
        border_radius="full",
        box_shadow="lg",
    )

# Main page
def index():
    # Use rx.cond to dynamically select the theme
    theme = rx.cond(
        State.is_dark_mode,
        MODERN_THEME["dark"],
        MODERN_THEME["light"],
    )

    return layout(
        rx.center(
            rx.vstack(
                # Hero Section
                rx.box(
                    rx.heading("Useful Applications", size="9", color=theme["primary"]),
                    rx.text("Explore the free tools below to get started.", size="5", color=theme["text"]),
                    text_align="center",
                    padding_bottom="2em",
                ),
                # Cards Section
                rx.flex(
                    rx.card(
                        rx.link(
                            rx.vstack(
                                rx.heading("Counter", size="7", color=theme["primary"]),
                                rx.text("Application to add or minus 1 or reset counter", size="4", color=theme["text"]),
                                spacing="2",
                                align="center",
                            ),
                            href="/counter",
                            _hover={"text_decoration": "none"},
                        ),
                        bg=theme["card_bg"],
                        padding="1.5em",
                        border_radius="12px",
                        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        _hover={"box_shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)", "transform": "translateY(-5px)", "transition": "all 0.3s ease"},
                    ),
                    rx.card(
                        rx.link(
                            rx.vstack(
                                rx.heading("Image to PDF", size="7", color=theme["primary"]),
                                rx.text("Application to convert any image to a PDF", size="4", color=theme["text"]),
                                spacing="2",
                                align="center",
                            ),
                            href="/imagetopdf",
                            _hover={"text_decoration": "none"},
                        ),
                        bg=theme["card_bg"],
                        padding="1.5em",
                        border_radius="12px",
                        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                        _hover={"box_shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)", "transform": "translateY(-5px)", "transition": "all 0.3s ease"},
                    ),
                    spacing="4",
                    justify="center",
                    align="center",
                    flex_wrap="wrap",
                    width="100%",
                ),
                spacing="6",
                align="center",
                width="100%",
                max_width="1200px",
                padding="2em",
            ),
            bg=theme["background"],
            height="100vh",
        ),
        theme_toggle(),  # Add the theme toggle button
    )

# Define application
app = rx.App()

# Add pages
app.add_page(index)
app.add_page(counter)
app.add_page(imagetopdf)