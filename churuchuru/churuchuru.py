import reflex as rx
from churuchuru.apps.counter import counter
from churuchuru.layout import layout

'''
Home Page
'''

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
Run page
'''
# Define application
app = rx.App()
# Add pages
app.add_page(index)
app.add_page(counter)

