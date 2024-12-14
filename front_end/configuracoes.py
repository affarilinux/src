from flet import icons, FilledButton, Row, Text, IconButton

from front_end.loja.LOJA import Loja


class Configuracoes():

    def __init__(self):

        self.loja_wg = Loja()

        # self.loja_db_cf = LojaDB()
        # self.loja_db_cf.ljdb_selecionar_nome_contagem()

    def config_criar_button_loja(self):

        from front_exe import Pagina

        def janela_loja(e):

            self.bt_loja()

        # Cria o botão com expand=True
        # lista botoes
        bt_loja = FilledButton(
            "LOJA",
            icons.ADD_HOME_WORK_ROUNDED,
            expand=True,
            adaptive=True,
            on_click=janela_loja
        )

        self.loja_row = Row(  # Cria o contêiner
            controls=[
                bt_loja
            ],
            expand=True
        )

        Pagina.PAGE.add(self.loja_row)  # Adiciona o contêiner à página

    # criar loja

    def bt_loja(self):

        from front_exe import Pagina

        ## configiracoes##
        self.config_remover_pagina()

        ### loja##
        self.loja_wg.lj_criar_pagina()

        # appbar mudar aba configuracoes

        def def_voltar(e):

            self.bt_loja_config()

        Pagina.PAGE.appbar.title = Text(
            "LOJA",
            color="#FFFF00"  # Yellow
        )

        Pagina.PAGE.appbar.leading = IconButton(
            icon=icons.ARROW_BACK,
            on_click=def_voltar,
            icon_color="#FFFF00"  # Yellow
        )

        Pagina.PAGE.update()

    # remover loja
    def bt_loja_config(self):

        from front_exe import Pagina

        # loja

        self.loja_wg.lj_remover_pagina()

        # configuracoes
        self.config_criar_pagina()

        Pagina.PAGE.appbar.title = Text(
            "CONFIGURAÇÕES",
            color="#FFFF00"  # Yellow
        )

        def ativar_drawer(e):

            Pagina.PAGE.drawer.open = True
            Pagina.PAGE.update()

        Pagina.PAGE.appbar.leading = IconButton(

            icon=icons.VIEW_LIST_ROUNDED,
            on_click=ativar_drawer,
            icon_color="#FFFF00"  # Yellow
        )

        Pagina.PAGE.update()
    ####################################################
    ####################################################

    def config_criar_pagina(self):

        self.config_criar_button_loja()

        from front_exe import Pagina
        Pagina.PAGE.update()

    def config_remover_pagina(self):

        from front_exe import Pagina

        # Pagina.PAGE.controls.remove(self.loja_row)  # Remove o contêiner
        if getattr(self, "loja_row", None) and self.loja_row in Pagina.PAGE.controls:
            Pagina.PAGE.controls.remove(self.loja_row)

        Pagina.PAGE.update()
