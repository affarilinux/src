from front_end.drawer import (NavegationDrawer)
from front_end.home import Home


class Pagina:

    PAGE = None


class FrontExe:

    def janela_home(self, page) -> None:

        Pagina.PAGE = page

        navd = NavegationDrawer()
        navd.criar_drawer()
        navd.desativar_drawer()

        home_jh = Home()
        home_jh.criar_appbar()

        Pagina.PAGE.update()
