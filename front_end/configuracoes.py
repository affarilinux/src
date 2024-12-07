from flet import AppBar, IconButton, icons, Text


class Configuracoes:

    def config_criar_appbar(self):

        from front_exe import Pagina

        #appbar so aparece se for assim
        Pagina.PAGE.appbar = AppBar(

            leading=IconButton(
                icons.ARROW_CIRCLE_RIGHT_SHARP,
                # on_click=ativar_drawer,
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

    def criar_pagina(self):

        self.config_criar_appbar()

        from front_exe import Pagina
        Pagina.PAGE.update()

    def remover_pagina(self):
