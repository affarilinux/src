from flet import (FloatingActionButton, Icons, ListView, ExpansionPanel,
                  ListTile, Text, Column, Row, IconButton, Icons,
                  ExpansionPanelList, Colors, TextField, DataTable,
                  DataColumn, AutoComplete, AutoCompleteSuggestion,
                  Container, FilledButton, CupertinoButton, ElevatedButton
                  )
import flet as ft
from front_entrada.entrada.db.entrada import EntradaDB
from front_entrada.entrada.db.subentrada_lista_entrada import SubEntradaDB

from front_entrada.entrada.menores import Menores
from front_entrada.entrada.editar_nome import EditarNome

from front_entrada.entrada.dialog_mais_entrada import DialogMaisentrada
from front_entrada.entrada.buttonsheet_adiconar import ButtonSheetAdicionar


class Listaentrada(
    EntradaDB, SubEntradaDB,
    Menores,  EditarNome,
    DialogMaisentrada, ButtonSheetAdicionar


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

    def botoes_lista(self):

        colu = Column([

            CupertinoButton(
                content=ft.Text("Filled CupertinoButton \n Filled CupertinoButton \n QT:8",
                                color=ft.Colors.RED),
                bgcolor=ft.Colors.PRIMARY,
                alignment=ft.alignment.top_left,
                border_radius=ft.border_radius.all(15),
                opacity_on_click=0.5,
                on_click=lambda e: print("Filled CupertinoButton clicked!"),
            ),

            CupertinoButton(
                content=ft.Text("Filled CupertinoButton \n Filled CupertinoButton \n QT:8",
                                color=ft.Colors.RED),
                bgcolor=ft.Colors.PRIMARY,
                alignment=ft.alignment.top_left,
                border_radius=ft.border_radius.all(15),
                opacity_on_click=0.5,
                on_click=lambda e: print("Filled CupertinoButton clicked!"),
            ),

        ],
            spacing=10
        )

        return colu

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

                    self.botoes_lista(),

                    Row([
                        IconButton(Icons.EDIT, tooltip="Editar",
                                   data=loja, on_click=editar_lista),
                        IconButton(Icons.DELETE, tooltip="Deletar",
                                   data=loja, on_click=remover_lista),
                        IconButton(Icons.PLAYLIST_ADD_SHARP, tooltip="Deletar",
                                   data=loja,
                                   on_click=lambda e: (self.ativar_item()))



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
    def listenter_entry_criar_pagina(self):

        from front_exe import Pagina

        self.entry_textfilder_filtro()
        # Supondo que varlist_loja é uma lista de tuplas [(loja_nome, status), ...]
        varlist_loja = self.lista_entrada_sqlite()  # Obtém os dados da tabela

        self.pd_criar_panellist(varlist_loja)
        self.pd_criar_button_lista()

        Pagina.PAGE.update()

    def listenter_entry_remover_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.remove(self.textfield_entry)
        Pagina.PAGE.floating_action_button = None

        Pagina.PAGE.remove(self.list_view_ent)

        Pagina.PAGE.update()
