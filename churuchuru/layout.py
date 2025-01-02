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

# Card component
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

def layout(*children, theme):
    return rx.box(
        rx.vstack(
            # Navigation bar
            rx.hstack(
                rx.hstack(
                    rx.link(
                        "ε(´｡•᎑•`)っ 🍜", 
                        href="/",
                        style={"color": theme["primary"]}),
                    spacing="3",
                ),
                width="100%",
                justify="center",
                padding_top="2em",
            ),
            
            # Main content
            rx.box(
                *children,
                width="100%",
                flex="1",  # This makes the content area expand
            ),
            
            # Footer
            rx.box(
                rx.hstack(
                    rx.text("Copyright © 2025 Churu Churu", style={"color": theme["primary"]}),
                    width="100%",
                    justify="center",
                    padding_y="2em",
                ),
                width="100%",
                bg=theme["background"],
            ),
            
            theme_toggle(),
            width="100%",
            align="center",
            min_height="100vh",  # Ensures minimum full viewport height
            spacing="0",  # Removes default spacing between vstack items
        ),
        bg=theme["background"],
    )