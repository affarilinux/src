from flet import (AppBar, Text, )
import flet as ft


class Home:

    def __init__(self) -> None:

        from front_exe import Pagina

        self.pagehome = Pagina.PAGE

    def criar_appbar(self):

        def ativar_drawer(e):

            from front_end.drawer import NavegationDrawer

            nd = NavegationDrawer()
            nd.ativar_drawer()

            self.pagehome.update()

        ######################################
        self.pagehome.appbar = AppBar(

            leading=ft.IconButton(
                ft.icons.ARROW_CIRCLE_RIGHT_SHARP,
                on_click=ativar_drawer,
                icon_color="#FFFF00"  # Yellow
            ),

            leading_width=40,

            title=Text(
                "HOME",
                color="#FFFF00"  # Yellow
            ),
            center_title=True,

            bgcolor="#4F4F4F"

        )
