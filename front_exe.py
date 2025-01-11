from flet import (NavigationDrawer, NavigationDrawerDestination, Container, Icons,
                  Icon, Divider)


from front_home.home import Home
from front_configuracao.configuracoes.configuracoes import Configuracoes
from front_end.appbar import AppBar
from front_entrada.entrada.lista_entrada import Listaentrada


class Pagina:

    PAGE = None


class FrontExe:

    index_janela = 1

    def __init__(self, page) -> None:
        super().__init__()

        Pagina.PAGE = page

        self.home_wg = Home()
        self.configuracoes_wg = Configuracoes()
        self.appbar_wg = AppBar()
        self.enter = Listaentrada()

        self.funcao_init()

    def funcao_init(self):

        self.criar_drawer()

        self.appbar_wg.appbar_config()
        self.appbar_wg.appbar_title("HOME")
        self.appbar_wg.appbar_leading_drawer()
        self.home_wg.home_criar_pagina()

        Pagina.PAGE.update()

    def criar_drawer(self):

        def ativar_index_janela(e):

            self.filtro_janela(e.control.selected_index)

        Pagina.PAGE.drawer = NavigationDrawer(


            on_change=ativar_index_janela,
            controls=[
                Container(height=12),
                NavigationDrawerDestination(  # 0
                    label="CONFIGURAÇÕES",
                    icon=Icons.SETTINGS_OUTLINED,
                    selected_icon=Icon(
                        Icons.SETTINGS_SUGGEST_ROUNDED
                    ),
                ),

                Divider(thickness=2),

                NavigationDrawerDestination(  # 1
                    icon=Icon(
                        Icons.HOME_WORK_OUTLINED
                    ),
                    label="HOME",
                    selected_icon=Icons.HOME_WORK,
                ),

                NavigationDrawerDestination(  # 2
                    icon=Icons.BUSINESS_CENTER_OUTLINED,
                    label="ENTRADA",
                    selected_icon=Icons.BUSINESS_CENTER,
                ),

                NavigationDrawerDestination(  # 3
                    icon=Icons.EXIT_TO_APP_OUTLINED,
                    label="SAIDA",
                    selected_icon=Icons.TRANSIT_ENTEREXIT,
                ),

                NavigationDrawerDestination(  # 3
                    icon=Icons.WORKSPACES_OUTLINE,
                    label="ESTOQUE",
                    selected_icon=Icons.WORKSPACES_FILLED,
                ),
            ],
        )

        Pagina.PAGE.drawer.open = False

    def filtro_janela(self, e_):

        print(FrontExe.index_janela)

        if e_ != FrontExe.index_janela:

            self.remover_janela()
            self.mudar_janela(e_)

            FrontExe.index_janela = e_

            print(FrontExe.index_janela)
        print("##**")

    def remover_janela(self):

        match FrontExe.index_janela:

            case 0:

                self.configuracoes_wg.config_remover_pagina()

            case 1:

                self.home_wg.home_remover_pagina()

            case 2:

                self.enter.listenter_entry_remover_pagina()

        Pagina.PAGE.update()

    def mudar_janela(self, e_1):

        match e_1:

            case 0:

                self.configuracoes_wg.config_criar_pagina()

                self.appbar_wg.appbar_title("CONFIGURAÇÕES")

            case 1:

                self.home_wg.home_criar_pagina()

                self.appbar_wg.appbar_title("HOME")

            case 2:

                self.enter.listenter_entry_criar_pagina()

                self.appbar_wg.appbar_title("ENTRADA")

        Pagina.PAGE.update()
