from flet import AppBar, IconButton, icons, Text, FilledButton, Row


class Loja:

    def loja_criar_appbar(self):

        from front_exe import Pagina

        def voltar_configuracoes(e):

            self.remover_pagina()

            Configuracoes.criar_pagina()

            Pagina.PAGE.update()

        # appbar so aparece se for com esse nome
        self.appbar = AppBar(

            leading=IconButton(
                icons.ARROW_CIRCLE_RIGHT_SHARP,
                on_click=voltar_configuracoes,
                icon_color="#FFFF00"  # Yellow
            ),

            leading_width=40,

            title=Text(
                "LOJA",
                color="#FFFF00"  # Yellow
            ),
            center_title=True,

            bgcolor="#4F4F4F"  # grey31

        )

        Pagina.PAGE.appbar = self.appbar

    def loja_criar_pagina(self):

        from front_exe import Pagina

        self.loja_criar_appbar()

        Pagina.PAGE.update()

    def loja_remover_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.appbar = None  # Remove AppBar

        Pagina.PAGE.update()


class Configuracoes(Loja):

    def config_criar_appbar(self):

        from front_exe import Pagina

        def ativar_drawer(e):

            Pagina.PAGE.drawer.open = True
            Pagina.PAGE.update()

        # appbar so aparece se for assim
        self.appbar = AppBar(

            leading=IconButton(
                icons.ARROW_CIRCLE_RIGHT_SHARP,
                on_click=ativar_drawer,
                icon_color="#FFFF00"  # Yellow
            ),

            leading_width=40,

            title=Text(
                "CONFIGURAÇÕES",
                color="#FFFF00"  # Yellow
            ),
            center_title=True,

            bgcolor="#4F4F4F"  # grey31

        )

        Pagina.PAGE.appbar = self.appbar

    def config_criar_button(self):

        from front_exe import Pagina

        def janela_loja(e):

            # self.loja()

            self.appbar.title = Text(
                "Loja",
                color="#FFFF00"  # Yellow
            )

            Pagina.PAGE.update()

        # Cria o botão com expand=True
        loja = FilledButton(
            "LOJA",
            icons.ADD_HOME_WORK_ROUNDED,
            expand=True,
            adaptive=True,
            on_click=janela_loja
        )

        self.loja_row = Row(  # Cria o contêiner
            controls=[
                loja
            ],
            expand=True
        )

        Pagina.PAGE.add(self.loja_row)  # Adiciona o contêiner à página

    def loja(self):

        self.remover_pagina()

        # self.loja_criar_pagina()
        from front_exe import Pagina
        Pagina.PAGE.update()

    def criar_pagina(self):

        self.config_criar_appbar()
        self.config_criar_button()

        from front_exe import Pagina
        Pagina.PAGE.update()

    def remover_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.appbar = None  # Remove AppBar
        # Pagina.PAGE.controls.remove(self.loja_row)  # Remove o contêiner
        if getattr(self, "loja_row", None) and self.loja_row in Pagina.PAGE.controls:
            Pagina.PAGE.controls.remove(self.loja_row)

        Pagina.PAGE.update()
