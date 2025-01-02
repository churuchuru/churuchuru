import reflex as rx
from churuchuru.components.colors import COLORS

'''
Layout
'''

# Define the app state
class Color(rx.State):
    is_dark_mode: bool = True  # Default to dark mode

    def toggle_theme(self):
        """Toggle between light and dark mode."""
        self.is_dark_mode = not self.is_dark_mode

# Theme toggle button with shadcn/ui style
def theme_toggle():
    return rx.button(
        rx.cond(Color.is_dark_mode, rx.icon(tag="moon"), rx.icon(tag="sun")),
        on_click=Color.toggle_theme,
        position="fixed",
        bottom="1.5em",
        right="1.5em",
        z_index="999",
        border_radius="full",
        bg=rx.cond(Color.is_dark_mode, COLORS["dark"]["card_bg"], COLORS["light"]["card_bg"]),  # Adjust background for light/dark theme
        backdrop_filter="blur(10px)",
        border="1px solid",
        border_color=rx.cond(Color.is_dark_mode, COLORS["dark"]["border"], COLORS["light"]["border"]),
        color=rx.cond(Color.is_dark_mode, "white", "black"),  # Adjust icon color for light/dark theme
        _hover={"transform": "scale(1.1)", "transition": "all 0.3s ease"},
    )

def layout(*children, theme):
    return rx.box(
        rx.vstack(
            # Navigation bar with theme styling
            rx.hstack(
                rx.hstack(
                    rx.link(
                        "Home",
                        href="/",
                        color=theme["primary"],  # Use theme color for the link
                        _hover={"color": theme["primary"], "text_decoration": "underline"},  # Hover effect
                    ),
                    spacing="3",
                ),
                width="100%",
                justify="center",
                padding_top="2em",
                padding_bottom="1em",
                bg=theme["card_bg"],  # Apply theme background to the navigation bar
                border_bottom=f"1px solid {theme['border']}",  # Add a border with theme color
                box_shadow="sm",  # Add a subtle shadow
            ),
            # Main content
            rx.box(
                *children,
                width="100%",
                color=theme["text"],  # Apply theme text color
            ),
            theme_toggle(),  # Add the theme toggle button
            width="100%",
            align="center",
        ),
        bg=theme["background"],  # Apply the theme background
        height="100vh",
        color=theme["text"],  # Apply theme text color globally
    )