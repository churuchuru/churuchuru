import reflex as rx

# Application
from churuchuru.apps.counter import counter
from churuchuru.apps.imagetopdf import imagetopdf

# Theme
from churuchuru.layout import layout
from churuchuru.components.colors import COLORS


# Define the app state
class State(rx.State):
    is_dark_mode: bool = True  # Default to dark mode

    def toggle_theme(self):
        """Toggle between light and dark mode."""
        self.is_dark_mode = not self.is_dark_mode

# Theme toggle button with shadcn/ui style
def theme_toggle():
    return rx.button(
        rx.cond(State.is_dark_mode, rx.icon(tag="moon"), rx.icon(tag="sun")),
        on_click=State.toggle_theme,
        position="fixed",
        bottom="1.5em",
        right="1.5em",
        z_index="999",
        border_radius="full",
        bg=rx.cond(State.is_dark_mode, COLORS["dark"]["card_bg"], COLORS["light"]["card_bg"]),  # Adjust background for light/dark theme
        backdrop_filter="blur(10px)",
        border="1px solid",
        border_color=rx.cond(State.is_dark_mode, COLORS["dark"]["border"], COLORS["light"]["border"]),
        color=rx.cond(State.is_dark_mode, "white", "black"),  # Adjust icon color for light/dark theme
        _hover={"transform": "scale(1.1)", "transition": "all 0.3s ease"},
    )

# Card component with shadcn/ui style
def app_card(title, description, href, theme):
    return rx.card(
        rx.link(
            rx.vstack(
                rx.heading(title, size="7", color=theme["primary"]),
                rx.text(description, size="4", color=theme["text"]),
                spacing="2",
                align="center",
            ),
            href=href,
            _hover={"text_decoration": "none"},
        ),
        bg=theme["card_bg"],
        padding="1.5em",
        border_radius="8px",
        border="1px solid",
        border_color=theme["border"],
        box_shadow="0 1px 3px rgba(0, 0, 0, 0.1)",
        _hover={
            "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
            "transform": "translateY(-2px)",
            "transition": "all 0.3s ease",
            "bg": theme["hover"],
        },
    )

# Main page with shadcn/ui-inspired design
def index():
    # Use rx.cond to dynamically select the theme
    theme = rx.cond(
        State.is_dark_mode,
        COLORS["dark"],
        COLORS["light"],
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
                    animate="fadeIn",  # Smooth fade-in animation
                ),
                # Cards Section
                rx.flex(
                    app_card("Counter", "Add, subtract, or reset a counter.", "/counter", theme),
                    app_card("Image to PDF", "Convert any image to a PDF.", "/imagetopdf", theme),
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