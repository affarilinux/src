from flet import (NavigationDrawer, NavigationDrawerDestination, Container, Icons,
                  Icon, Divider)


class NavegationDrawer:

    def __init__(self) -> None:
        from front_exe import Pagina

        self.pagedrawer = Pagina.PAGE

    def criar_drawer(self):
        def ativar_index_janela(e):

            self.filtro_janela(e.control.selected_index)

        ###############################################
        self.pagedrawer.drawer = NavigationDrawer(
            # self.drawer = NavegationDrawer(

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

        # self.pagedrawer.add(self.drawer)

    def desativar_drawer(self):

        self.pagedrawer.drawer.open = False

    def ativar_drawer(self):

        self.pagedrawer.drawer.open = True

    def filtro_janela(self, e_):

        from front_exe import FrontExe

        if e_ != FrontExe.index_janela:

            self.remover_janela()

    def remover_janela(self,):

    def mudar_janela(self, e_1):

        if e_ == 0:

        elif e_ == 1:

            # remover
            # criar
            from front_end.home import Home

            home = Home()
            home.criar_appbar()
