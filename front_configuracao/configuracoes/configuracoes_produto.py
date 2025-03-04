from flet import Text, IconButton, icons


class ConfiguracoesProduto:

    # criar loja
    def bt_produto(self):

        from front_exe import Pagina

        ## configiracoes##
        self.config_remover_pagina()

        ### loja##
        self.lista_prod.pd_criar_pagina()

        # appbar mudar aba configuracoes

        def def_voltar(e):

            self.bt_produto_config()

        Pagina.PAGE.appbar.title = Text(
            "LISTA PRODUTOS",
            color="#FFFF00"  # Yellow
        )

        Pagina.PAGE.appbar.leading = IconButton(
            icon=icons.ARROW_BACK,
            on_click=def_voltar,
            icon_color="#FFFF00"  # Yellow
        )

        Pagina.PAGE.update()

    # remover loja
    def bt_produto_config(self):

        from front_exe import Pagina

        # loja

        self.lista_prod.pd_remover_pagina()

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
