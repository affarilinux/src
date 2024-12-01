from flet import (AppBar, Text, )
import flet as ft


class Home:

    def criar_appbar(self):

        from front_exe import Pagina

        Pagina.PAGE.appbar = AppBar(

            leading=ft.IconButton(
                ft.icons.ARROW_CIRCLE_RIGHT_SHARP,
                # on_click=,
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
