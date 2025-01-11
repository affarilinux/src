from flet import (Column, Text, Container, AutoComplete, AutoCompleteSuggestion,
                  TextField, FilledButton, BottomSheet, Row)

from front_entrada.entrada.db.subentreda_btsheet_adicionar import (
    SubEntradaBtsheetAdicionarDB)


class ButtonSheetAdicionar(SubEntradaBtsheetAdicionarDB):

    lista_subproduto = []

    def atualizar_subprodutos(self, produto):

        ButtonSheetAdicionar.lista_subproduto = (
            self.sheadic_select_listaquery_subentrada(produto))

        print(ButtonSheetAdicionar.lista_subproduto)

    def adicionar_itens_lista(self):

        return Column(
            controls=[
                Column(
                    controls=[
                        Text(value="Produto:", size=16),
                        Container(
                            content=AutoComplete(
                                suggestions=self.sheadic_select_lista_entrada(),
                                on_select=lambda e: self.atualizar_subprodutos(
                                    e.control.suggestions[e.control.selected_index].key
                                ),
                            ),
                            expand=True,
                        ),
                    ]
                ),
                Column(
                    controls=[
                        Text(value="Subproduto:", size=16),
                        Container(
                            content=AutoComplete(
                                suggestions=ButtonSheetAdicionar.lista_subproduto,
                                on_select=lambda e: print(
                                    e.control.selected_index, e.selection),

                            ),
                            expand=True,
                        ),
                    ]
                ),
                TextField(
                    adaptive=True,
                    label="Adaptive",
                ),
                Row([
                    FilledButton(
                        "Cancelar",
                        on_click=self.close_bottom_sheet,
                    ),
                    FilledButton(
                        "Aplicar"
                    ),


                ])
            ]
        )

    def close_bottom_sheet(self, e):
        from front_exe import Pagina
        if self.bs:
            self.bs.open = False
            Pagina.PAGE.update()

    def ativar_item(self):
        from front_exe import Pagina

        self.bs = BottomSheet(
            open=True,
            content=Container(
                padding=20,
                content=Column(
                    controls=[
                        self.adicionar_itens_lista(),

                    ]
                ),
            ),
        )
        Pagina.PAGE.overlay.append(self.bs)
        Pagina.PAGE.update()
