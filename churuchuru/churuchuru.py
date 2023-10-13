"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://www.churuchuru.com/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Churu Churu", font_size="2em"),
            # rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "www.churuchuru.com",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index,
             # Title of website (beside favicon) 
             title='Churu Churu')
app.compile()
