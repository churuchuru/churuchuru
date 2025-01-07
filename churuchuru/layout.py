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
                    color="#FFFFFF",  # White by default
                    text_align="left",
                    margin_bottom="0.5em",
                    font_weight="bold",
                    transition="color 0.3s ease",  # Smooth transition for header color
                    _hover={
                        "color": theme["primary"],  # Change to primary color on hover
                    },
                ),
                rx.text(
                    description,
                    color="#D1D5DB",  # Light grey for description (always)
                    text_align="left",
                    font_size="1em",
                    opacity="0.8",
                    line_height="1.6",  
                ),
                spacing="4",
                align="start",
                padding="2em",
            ),
            _hover={
                "box_shadow": "0 8px 16px rgba(0, 0, 0, 0.3)",  # Enhanced shadow on hover
                "transform": "translateY(-6px)",  # Lift effect on hover
                "transition": "all 0.3s ease",
                "border_color": theme["primary"],  # Border color changes to primary on hover
            },
            height="100%",
            # width="100%",
            max_width="600px",  # Reduced width for compactness
            border_radius="xl",
            border=f"2px solid {theme['card_bg']}",  # Default border color uses card_bg
            background_color="transparent",  # Transparent background always
            transition="all 0.3s ease-in-out",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",  # Subtle shadow by default
            position="relative",
            overflow="hidden",
            margin="0 auto",  # Center the card horizontally
            # display="flex",
            justify_content="center",  # Center content horizontally
            align_items="center",  # Center content vertically
        ),
        href=href,
        text_decoration="none",
        margin="1em",  # Add space between cards
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