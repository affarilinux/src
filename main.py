from flet import Page, app

from front_exe import FrontExe

# Inicializa a aplicação


def main(page: Page):

    page.adaptive = True
    page.bgcolor = "#808080"  # Gray
    APP_EXE = FrontExe(page)


if __name__ == "__main__":
    app(target=main)
