from flet import (FloatingActionButton, Icons, ListView, ExpansionPanel,
                  ListTile, Text, Column, Row, IconButton, Icons,
                  ExpansionPanelList, Colors, TextField, DataTable,
                  DataColumn
                  )
import flet as ft
from front_entrada.entrada.db.entrada import EntradaDB
from front_entrada.entrada.db.subentrada_lista_entrada import SubEntradaDB

from front_entrada.entrada.menores import Menores
from front_entrada.entrada.editar_nome import EditarNome

from front_entrada.entrada.dialog_mais_entrada import DialogMaisentrada
from front_entrada.entrada.dialog_lista_subentrada import DialogMaisLista


class Listaentrada(
    EntradaDB, SubEntradaDB,
    Menores,  EditarNome,
    DialogMaisentrada, DialogMaisLista


):
    def __init__(self):
        super().__init__()

        SubEntradaDB.__init__(self)

    def entry_textfilder_filtro(self):

        from front_exe import Pagina

        def filtrar(e):

            self.text_filtro_entrada(self.textfield_entry.value)

        self.textfield_entry = TextField(
            label="Escreva um nome:",
            on_change=filtrar

        )

        Pagina.PAGE.add(self.textfield_entry)

    def lista_datatable_produtos(self, loja):

        lista = []

        enter = self.et_selecionar_index_nome(loja[0])

        print(self.subent_query_lista(enter))

        subentradas = self.subent_query_lista(enter)

        # Cria as linhas da tabela dinamicamente
        for subentrada in subentradas:
            # Assuma que subentrada contém: (ID_subentrada, sub_nome, quantidade)
            id_subentrada, sub_nome, quantidade = subentrada

            # Adiciona uma nova linha (DataRow) à lista
            lista.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.IconButton(ft.icons.EDIT, tooltip=f"Editar ID {
                                    id_subentrada}", data=id_subentrada)),
                        ft.DataCell(ft.Text(sub_nome)),  # Nome do subitem
                        ft.DataCell(ft.Text(str(quantidade))),  # Quantidade
                    ]
                )
            )
        """ft.DataRow(
                cells=[
                    ft.DataCell(IconButton(
                        Icons.EDIT, tooltip="Editar", data=loja)),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("Smith")),
                    ft.DataCell(ft.Text("43")),
                ],
            ),
            ft.DataRow(
                cells=[
                    # Preenchendo a coluna "Editar"
                    ft.DataCell(IconButton(Icons.EDIT)),
                    ft.DataCell(ft.Text("Jack")),
                    ft.DataCell(ft.Text("Brown")),
                    ft.DataCell(ft.Text("19")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(IconButton(Icons.EDIT)),
                    ft.DataCell(ft.Text("Alice")),
                    ft.DataCell(ft.Text("Wong")),
                    ft.DataCell(ft.Text("25")),
                ],
            ),"""

        return lista

    def pd_criar_panellist(self, varlist_loja):

        from front_exe import Pagina

        def editar_lista(e):
            self.dialogo_editar_produto(e.control.data[0])

        def remover_lista(e):
            self.remover_nome_entrada(e.control.data[0])

        colors = ["#008000", "#20B2AA", "#708090", "#B8860B", "#4B0082"]

        panels = [
            ExpansionPanel(
                bgcolor=colors[i % len(colors)],
                header=ListTile(title=Text(loja[0])),
                content=Column([
                    Column([
                        Row([

                            IconButton(Icons.EDIT, tooltip="Editar",
                                       data=loja,  # on_click=editar_lista
                                       ),



                            Text("acabamento", expand=True),
                            Text("registro", expand=True),
                            Text("24", expand=True),




                        ], ft.MainAxisAlignment.SPACE_BETWEEN),

                        DataTable(
                            columns=[
                                DataColumn(Text("Editar")),
                                DataColumn(Text("Nome")),
                                DataColumn(Text("Característica")),
                                DataColumn(
                                    Text("QT/unid"), numeric=True),
                            ],
                            rows=self.lista_datatable_produtos(loja)


                        )

                    ]),

                    Row([
                        IconButton(Icons.EDIT, tooltip="Editar",
                                   data=loja, on_click=editar_lista),
                        IconButton(Icons.DELETE, tooltip="Deletar",
                                   data=loja, on_click=remover_lista),
                        IconButton(Icons.PLAYLIST_ADD_ROUNDED, tooltip="Lista",
                                   data=loja,  # on_click=remover_lista
                                   ),
                    ], alignment="start"),
                ]),
            ) for i, loja in enumerate(varlist_loja)
        ]

        def handle_scroll(e):
            if e.scroll_delta is not None:
                visible = e.scroll_delta < 0
                Pagina.PAGE.floating_action_button.visible = visible
                Pagina.PAGE.update()

        self.list_view_ent = ListView(
            expand=True, spacing=10, padding=10,
            controls=[ExpansionPanelList(
                expand_icon_color=Colors.AMBER,
                elevation=8,
                divider_color=Colors.AMBER,
                controls=panels)],
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
