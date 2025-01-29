from flet import (FloatingActionButton, Icons, ListView, ExpansionPanel,
                  ListTile, Text, Column, Row, IconButton, Icons,
                  ExpansionPanelList, Colors, TextField, CupertinoButton,
                  alignment, border_radius

                  )
from front_entrada.entrada.db.entrada import EntradaDB
from front_entrada.entrada.db.subentrada_lista_entrada import SubEntradaDB

from front_entrada.entrada.menores import Menores
from front_entrada.entrada.editar_nome import EditarNome

from front_entrada.entrada.dialog_mais_entrada import DialogMaisentrada
from front_entrada.entrada.buttonsheet_adiconar import ButtonSheetAdicionar
from front_entrada.entrada.dialog_editar_apagar import DialogEditarApagar


class Listaentrada(
    EntradaDB, SubEntradaDB,
    Menores,  EditarNome,
    DialogMaisentrada, ButtonSheetAdicionar, DialogEditarApagar


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

    def botoes_cupetino(
            self, e, loja, nome_produto, nome_subproduto, quantidade):
        DialogEditarApagar.lista_if_edit["entrada"] = loja
        DialogEditarApagar.lista_if_edit["produto"] = nome_produto
        DialogEditarApagar.lista_if_edit["subproduto"] = nome_subproduto
        DialogEditarApagar.lista_if_edit["quantidade"] = quantidade

        # Chama diretamente o construtor

        self.dialogo_subentrada()

    def botoes_lista(self, loja):

        resultados = self.sheadic_select_query_tripla(loja[0])

        # Cria uma lista de CupertinoButton dinamicamente com base nos resultados
        botoes = [
            CupertinoButton(
                content=Text(
                    f"{nome_produto} \n {nome_subproduto} \n QT:{quantidade}",
                    color=Colors.RED,
                ),
                bgcolor=Colors.PRIMARY,
                alignment=alignment.top_left,
                border_radius=border_radius.all(15),
                opacity_on_click=0.5,
                # Captura os valores atuais no loop com argumentos padrão na lambda
                on_click=lambda e, np=nome_produto, ns=nome_subproduto, qt=quantidade: (
                    self.botoes_cupetino(e, loja[0], np, ns, qt)
                )
            )
            for nome_produto, nome_subproduto, quantidade in resultados
        ]

        # Retorna a coluna com os botões criados
        colu = Column(
            botoes,
            spacing=10,
        )

        return colu

    def pd_criar_panellist(self, varlist_loja):

        from front_exe import Pagina

        def editar_lista(e):
            self.dialogo_editar_produto(e.control.data[0])

        colors = ["#008000", "#20B2AA", "#708090", "#B8860B", "#4B0082"]

        panels = [
            ExpansionPanel(
                bgcolor=colors[i % len(colors)],
                header=ListTile(title=Text(loja[0])),
                content=Column([

                    self.botoes_lista(loja),

                    Row([
                        IconButton(Icons.EDIT, tooltip="Editar",
                                   data=loja, on_click=editar_lista),

                        IconButton(Icons.DELETE, tooltip="Deletar",
                                   data=loja,
                                   on_click=lambda e: self.remover_nome_entrada(
                                       e.control.data[0])),

                        IconButton(Icons.PLAYLIST_ADD_SHARP, tooltip="Adicionar",
                                   data=loja,
                                   on_click=lambda e: (
                                       ButtonSheetAdicionar.__init__(self),
                                       self.ativar_item(e.control.data))
                                   )



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
