from flet import AppBar as FletAppBar, IconButton, icons, Text


class AppBar:

    def appbar_config(self):
        from front_exe import Pagina

        apb = FletAppBar(
            leading_width=40,
            center_title=True,
            bgcolor="#4F4F4F"  # Grey
        )

        Pagina.PAGE.appbar = apb

    def appbar_title(self, title_):

        from front_exe import Pagina

        Pagina.PAGE.appbar.title = Text(
            title_,
            color="#FFFF00"  # Yellow
        )

    def appbar_leading_drawer(self):

        from front_exe import Pagina

        def ativar_drawer(e):
            Pagina.PAGE.drawer.open = True
            Pagina.PAGE.update()

        Pagina.PAGE.appbar.leading = IconButton(
            icon=icons.VIEW_LIST_ROUNDED,
            on_click=ativar_drawer,
            icon_color="#FFFF00"  # Yellow
        )
