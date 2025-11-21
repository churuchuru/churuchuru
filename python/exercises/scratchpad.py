import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Python Scratchpad
    [Churu Churu Website](https://www.churuchuru.com) | [Churu Churu Github Repo](https://github.com/churuchuru/churuchuru)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Feel free to use this to run Python code quickly in your browser
    """)
    return


@app.cell(hide_code=True)
def _():
    print("Welcome to Churu Churu Scratchpad")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
