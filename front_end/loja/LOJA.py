
from flet import (FloatingActionButton, Icons, ListView, ExpansionPanel,
                  ListTile, Text, Column, Row, IconButton, Icons,
                  ExpansionPanelList, Colors
                  )

from banco_sqlite.loja import LojaDB

from front_end.loja.dialog_mais import DialogMais
from front_end.loja.editar_nome import EditarNome


class Loja(DialogMais, LojaDB, EditarNome):

    def lj_criar_panellist(self):
        from front_exe import Pagina

        def editar_lista(e):

            self.dialogo_editar()

        varlist_loja = self.ljdb_selecionar_nome_contagem()

        # Lista de cores para os painéis
        colors = [
            "#00FF7F",  # SpringGreen
            "#20B2AA",  # LightSeaGreen
            "#708090",  # SlateGray
            "#B8860B",  # DarkGoldenrod
            "#4B0082"  # Indigo

        ]

        # Lista para armazenar os painéis
        panels = []

        # Criando os painéis no loop
        for i, loja_nome in enumerate(varlist_loja):
            exp = ExpansionPanel(
                bgcolor=colors[i % len(colors)],
                header=ListTile(
                    title=Text(f" {loja_nome[0]}")
                ),
            )

            # Adicionando múltiplos IconButtons no conteúdo
            exp.content = Column(
                [
                    Row(
                        [
                            IconButton(
                                Icons.EDIT,
                                tooltip="Editar",
                                data=loja_nome,
                                on_click=editar_lista
                            ),
                            IconButton(
                                Icons.DELETE,
                                tooltip="Deletar",
                                data=loja_nome,
                            ),

                        ],
                        alignment="start",
                    ),
                ]
            )

            # Adiciona o painel à lista de painéis
            panels.append(exp)

        panel = ExpansionPanelList(
            expand_icon_color=Colors.AMBER,
            elevation=8,
            divider_color=Colors.AMBER,
            controls=panels

        )
        # ****************************************
        # rolo da lista

        def handle_scroll(e):

            # Desaparecer o botão imediatamente quando rolar para baixo
            if e.scroll_delta is not None:

                if e.scroll_delta > 0:  # rola para baixo

                    Pagina.PAGE.floating_action_button.visible = False
                    Pagina.PAGE.update()

                elif e.scroll_delta < 0:  # rola para cima

                    Pagina.PAGE.floating_action_button.visible = True
                    Pagina.PAGE.update()

        self.list_view = ListView(
            expand=True,
            spacing=10,
            padding=10,
            controls=[panel],
            on_scroll=handle_scroll,
        )

        Pagina.PAGE.add(self.list_view)

    ##############################################
    # butao mais

    def lj_criar_button_lista(self):
        from front_exe import Pagina

        def salvar_banco(e):

            # dialog = DialogMais()
            # dialog.dialogo()
            self.dialogo()

        Pagina.PAGE.floating_action_button = FloatingActionButton(
            icon=Icons.ADD,
            on_click=salvar_banco,
            bgcolor="#FFFF00",  # Yellow
            foreground_color="#4F4F4F",  # Grey color
            visible=True  # Define inicialmente visível
        )

    #################################################
    # class

    def lj_criar_pagina(self):

        from front_exe import Pagina

        self.lj_criar_panellist()
        self.lj_criar_button_lista()
        Pagina.PAGE.update()

    def lj_remover_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.floating_action_button = None

        Pagina.PAGE.remove(self.list_view)

        Pagina.PAGE.update()
