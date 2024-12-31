import reflex as rx

'''
Main Application
'''

# Menu bar
def layout(*children):
    return rx.box(
        rx.vstack(
            # Navigation bar
            rx.hstack(
                rx.heading("My App"),
                rx.hstack(
                    rx.link("Home", href="/"),
                    rx.link("Counter", href="/counter"),
                    spacing="3",
                ),
                width="100%",
                justify="between",
                padding="4",
            ),
            # Main content
            rx.box(
                *children,
                padding_top="6em",
            ),
        )
    )

# Main page
def index():
    return layout(
        rx.center(
        rx.flex(
            rx.card(
                rx.link(
                    rx.vstack(
                        rx.heading("Counter"),
                        rx.text("Application to add or minus 1 or reset counter"),
                        spacing="2",
                        align="center",
                    ),
                    href="/counter"
                ),
                as_child=True,
            ),
            spacing="2",
            justify="center",
            align="center",
            flex_wrap="wrap",
            width="100%",
        ),
        height="100vh",
    )
    )

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
    return rx.center(
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


'''
Run page
'''
# Define application
app = rx.App()
# Add pages
app.add_page(index)
app.add_page(counter)

