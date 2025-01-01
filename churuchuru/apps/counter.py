import reflex as rx
from churuchuru.layout import layout

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
    return layout(rx.center(
        rx.vstack(
            rx.heading("Counter"),
            rx.hstack(
                rx.button(
                    "Decrement", 
                    color_scheme="ruby",
                    on_click=State.decrement,
                ),
                rx.heading(State.count, font_size="2em"),
                rx.button(
                    "Increment",
                    color_scheme="grass", 
                    on_click=State.increment,
                ),
                spacing="4",
            ),
            rx.button(
                "Reset",
                color_scheme="gray", 
                on_click=State.reset_count,
            ),
            spacing="4",
            align="center",
        ),
        height="100vh",
    )
    )

