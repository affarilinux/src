"""from flet import (Column, Text, Container, AutoComplete,
                  TextField, FilledButton, BottomSheet, Row,
                  Dropdown, dropdown)

from front_entrada.entrada.db.subentreda_btsheet_adicionar import (
    SubEntradaBtsheetAdicionarDB)


class ButtonSheetAdicionar(SubEntradaBtsheetAdicionarDB):

    lista_subproduto = []

    def atualizar_subprodutos(self, produto):

        from front_exe import Pagina

        ButtonSheetAdicionar.lista_subproduto = (
            self.sheadic_select_listaquery_subentrada(produto))

        print(ButtonSheetAdicionar.lista_subproduto)

        Pagina.PAGE.update()

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
                        Dropdown(
                            expand=True,
                            options=ButtonSheetAdicionar.lista_subproduto
                        )
                    ]
                ),
                TextField(
                    adaptive=True,
                    label="Quantidade:",
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
        Pagina.PAGE.update()"""

from flet import (Column, Text, Container, AutoComplete,
                  TextField, FilledButton, BottomSheet, Row,
                  Dropdown, dropdown, Ref)

from front_entrada.entrada.db.subentreda_btsheet_adicionar import (
    SubEntradaBtsheetAdicionarDB)


class ButtonSheetAdicionar(SubEntradaBtsheetAdicionarDB):
    lista_subproduto = []
    dropdown_ref = Ref[Dropdown]()  # Adiciona uma referência ao Dropdown

    def atualizar_subprodutos(self, produto):
        from front_exe import Pagina

        # Atualiza a lista de subprodutos
        ButtonSheetAdicionar.lista_subproduto = (
            self.sheadic_select_listaquery_subentrada(produto)
        )

        # Cria as opções do Dropdown a partir da lista de strings
        self.dropdown_ref.current.options = [
            dropdown.Option(key=item, text=item) for item in ButtonSheetAdicionar.lista_subproduto
        ]
        self.dropdown_ref.current.update()  # Força a atualização do Dropdown

        Pagina.PAGE.update()


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
                        Dropdown(
                            ref=self.dropdown_ref,  # Associa a referência ao Dropdown
                            expand=True,
                            options=[]
                        )
                    ]
                ),
                TextField(
                    adaptive=True,
                    label="Quantidade:",
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
