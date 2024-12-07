from flet import (NavigationDrawer, NavigationDrawerDestination, Container, Icons,
                  Icon, Divider)


from front_end.home import Home
from front_end.configuracoes import Configuracoes


class Pagina:

    PAGE = None


class FrontExe:

    index_janela = 1

    def __init__(self, page) -> None:
        super().__init__()

        Pagina.PAGE = page

        self.home_wg = Home()
        self.configuracoes_wg = Configuracoes()

        self.funcao_init()

    def funcao_init(self):

        self.criar_drawer()
        self.desativar_drawer()

        self.home_wg.criar_pagina()

        Pagina.PAGE.update()

    def criar_drawer(self):

        def ativar_index_janela(e):

            self.filtro_janela(e.control.selected_index)

        Pagina.PAGE.drawer = NavigationDrawer(


            on_change=ativar_index_janela,
            controls=[
                Container(height=12),
                NavigationDrawerDestination(
                    label="CONFIGURAÇÕES",
                    icon=Icons.SETTINGS_OUTLINED,
                    selected_icon=Icon(
                        Icons.SETTINGS_SUGGEST_ROUNDED
                    ),
                ),
                Divider(thickness=2),
                NavigationDrawerDestination(
                    icon=Icon(
                        Icons.HOME_WORK_OUTLINED
                    ),
                    label="HOME",
                    selected_icon=Icons.HOME_WORK,
                ),
                NavigationDrawerDestination(
                    icon=Icon(Icons.PHONE_OUTLINED),
                    label="Item 3",
                    selected_icon=Icons.PHONE,
                ),
            ],
        )

    def desativar_drawer(self):

        Pagina.PAGE.drawer.open = False

    def ativar_drawer(self):

        Pagina.PAGE.drawer.open = True

    def filtro_janela(self, e_):

        if e_ != FrontExe.index_janela:

            self.remover_janela()
            self.mudar_janela(e_)

            FrontExe.index_janela = e_

    def remover_janela(self):

        match FrontExe.index_janela:

            # case 0:

            case 1:

                self.home_wg.remover_pagina()

    def mudar_janela(self, e_1):

        match e_1:

            case 0:

                self.configuracoes_wg.criar_pagina()

            case 1:

                self.home_wg.criar_pagina()
