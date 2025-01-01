import reflex as rx

'''
Layout
'''

# Menu bar
def layout(*children):
    return rx.box(
        rx.vstack(
            # Navigation bar
            rx.hstack(
                rx.hstack(
                    rx.link("Home", href="/"),
                    # rx.link("Counter", href="/counter"),
                    spacing="3",
                ),
                width="100%",
                justify="center",
                padding_top="2em",
            ),
            # Main content 
            rx.box(
                *children,
                # padding_top="6em",
                width="100%",
            ),
            width="100%",
            align="center",
        ),
        height="100vh",
    )
