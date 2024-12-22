from flet import (FloatingActionButton, Icons, ListView, ExpansionPanel,
                  ListTile, Text, Column, Row, IconButton, Icons,
                  ExpansionPanelList, Colors, TextField
                  )


from banco_sqlite.entrada import EntradaDB
from front_end.entrada.menores import Menores
from front_end.entrada.dialog_mais import DialogMais


class Listaentrada(
    EntradaDB, Menores, DialogMais
):

    def entry_textfilder_filtro(self):

        from front_exe import Pagina

        def filtrar(e):

            self.text_filtro_entrada(self.textfield_entry.value)

        self.textfield_entry = TextField(
            label="Escreva um nome:",
            on_change=filtrar

        )

        Pagina.PAGE.add(self.textfield_entry)

    def pd_criar_panellist(self, varlist_loja):
        from front_exe import Pagina

        def editar_lista(e):

            titulo = e.control.data  # Recupera o índice armazenado no botão

            # Chama a função com o índice correto
            self.dialogo_editar_produto(titulo[0])

        def remover_lista(e):

            titulo_1 = e.control.data  # Recupera o índice armazenado no botão

            self.remover_nome_entrada(titulo_1[0])

        # Lista de cores para os painéis
        colors = [
            "#008000",  # Green
            "#20B2AA",  # LightSeaGreen
            "#708090",  # SlateGray
            "#B8860B",  # DarkGoldenrod
            "#4B0082"  # Indigo

        ]

        # Lista para armazenar os painéis
        panels = []

        for i, (loja_nome) in enumerate(varlist_loja):

            exp = ExpansionPanel(
                bgcolor=colors[i % len(colors)],
                header=ListTile(
                    title=Text(f" {loja_nome[0]}")
                ),
            )

            # Adicionando os botões ao conteúdo do painel
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
                                on_click=remover_lista
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

        self.list_view_ent = ListView(
            expand=True,
            spacing=10,
            padding=10,
            controls=[panel],
            on_scroll=handle_scroll,
        )

        Pagina.PAGE.add(self.list_view_ent)

    ##############################################
    # butao mais

    def pd_criar_button_lista(self):
        from front_exe import Pagina

        def salvar_banco(e):

            self.dialogo_entrada()

        Pagina.PAGE.floating_action_button = FloatingActionButton(
            icon=Icons.ADD,
            on_click=salvar_banco,
            bgcolor="#FFFF00",  # Yellow
            foreground_color="#4F4F4F",  # Grey color
            visible=True  # Define inicialmente visível
        )

    #################################################
    # class
    def entry_criar_pagina(self):

        from front_exe import Pagina

        self.entry_textfilder_filtro()
        # Supondo que varlist_loja é uma lista de tuplas [(loja_nome, status), ...]
        varlist_loja = self.lista_entrada_sqlite()  # Obtém os dados da tabela

        self.pd_criar_panellist(varlist_loja)
        self.pd_criar_button_lista()

        Pagina.PAGE.update()

    def entry_remover_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.remove(self.textfield_entry)
        Pagina.PAGE.floating_action_button = None

        Pagina.PAGE.remove(self.list_view_ent)

        Pagina.PAGE.update()