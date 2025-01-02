import reflex as rx

# Theme
from churuchuru.layout import layout, Color
from churuchuru.components.colors import COLORS

'''
Counter Application
'''

# Backend
# Defines all variables and function
class State(rx.State):
    count: int = 0

    # Event handlers (functions) that modify state variables
    # Called in response to user actions (events)
    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset_count(self):
        self.count = 0


# Counter App
def counter() -> rx.Component:
    # Use rx.cond to dynamically select the theme
    theme = rx.cond(
        Color.is_dark_mode,
        COLORS["dark"],
        COLORS["light"],
    )
        
    return layout(
        rx.center(
            rx.vstack(
                rx.heading("Counter", color=theme["primary"]),  # Apply theme color to heading
                rx.hstack(
                    rx.button(
                        "Decrement",
                        on_click=State.decrement,
                        bg=theme["card_bg"],  # Apply theme background to button
                        color=theme["text"],  # Apply theme text color to button
                        border=f"1px solid {theme['border']}",  # Apply theme border to button
                        _hover={"bg": theme["hover"]},  # Apply theme hover effect
                    ),
                    rx.heading(
                        State.count,
                        font_size="2em",
                        color=theme["text"],  # Apply theme text color to count
                    ),
                    rx.button(
                        "Increment",
                        on_click=State.increment,
                        bg=theme["card_bg"],  # Apply theme background to button
                        color=theme["text"],  # Apply theme text color to button
                        border=f"1px solid {theme['border']}",  # Apply theme border to button
                        _hover={"bg": theme["hover"]},  # Apply theme hover effect
                    ),
                    spacing="4",
                ),
                rx.button(
                    "Reset",
                    on_click=State.reset_count,
                    bg=theme["card_bg"],  # Apply theme background to button
                    color=theme["text"],  # Apply theme text color to button
                    border=f"1px solid {theme['border']}",  # Apply theme border to button
                    _hover={"bg": theme["hover"]},  # Apply theme hover effect
                ),
                spacing="4",
                align="center",
            ),
            bg=theme["background"],  # Apply theme background to the page
            height="100vh",
        ),
        theme=theme,  # Pass the theme to layout
    )