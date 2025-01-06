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
def app_card(title: str, description: str, href: str, theme: dict) -> rx.Component:
    return rx.link(
        rx.card(
            rx.vstack(
                rx.heading(
                    title,
                    size="6",
                    color=theme["primary"],
                    text_align="center",
                    margin_bottom="0.5em",
                ),
                rx.text(
                    description,
                    color=theme["text"],
                    text_align="center",
                    font_size="1em",
                    opacity="0.8",
                ),
                spacing="4",
                align="center",
                padding="2em",  # Increased padding for better spacing
            ),
            _hover={
                "box_shadow": "0 8px 12px rgba(0, 0, 0, 0.2)",  # Enhanced shadow
                "transform": "translateY(-4px)",  # More pronounced lift
                "transition": "all 0.3s ease",
                "bg": theme["hover"],
            },
            height="100%",
            width="100%",  # Ensure cards take full width of their container
            border_radius="xl",
            border=f"1px solid {theme['border']}",
            background_color=theme["card_bg"],
            transition="all 0.2s ease-in-out",
        ),
        href=href,
        text_decoration="none",
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