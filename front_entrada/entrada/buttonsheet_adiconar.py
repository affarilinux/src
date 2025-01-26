
from flet import (Column, Text, Container, AutoComplete,
                  TextField, FilledButton, BottomSheet, Row,
                  Dropdown, dropdown, Ref)

from front_entrada.entrada.db.subentreda_btsheet_adicionar import (
    SubEntradaBtsheetAdicionarDB)


class ButtonSheetAdicionar(SubEntradaBtsheetAdicionarDB):

    lista_subproduto_adic = []
    dropdown_ref_adic = Ref[Dropdown]()  # Adiciona uma referência ao Dropdown

    lista_if_adic = {
        "produto": "", "subproduto": "", "quantidade": ""
    }

    def __init__(self):
        super().__init__()

        self.limpar_lista_classe()

    def atualizar_subprodutos(self, produto, selecao):
        from front_exe import Pagina

        # Atualiza a lista de subprodutos
        ButtonSheetAdicionar.lista_subproduto_adic = (
            self.sheadic_select_listaquery_subentrada(produto)
        )

        # Cria as opções do Dropdown a partir da lista de strings
        self.dropdown_ref_adic.current.options = [
            dropdown.Option(key=item, text=item) for item in ButtonSheetAdicionar.lista_subproduto_adic
        ]
        self.dropdown_ref_adic.current.update()  # Força a atualização do Dropdown

        ButtonSheetAdicionar.lista_if_adic["produto"] = selecao
        ButtonSheetAdicionar.lista_if_adic["subproduto"] = ""

        Pagina.PAGE.update()

    def lista_subproduto_adic_dropdawn(self, value):

        if value != "":

            ButtonSheetAdicionar.lista_if_adic["subproduto"] = value

    def lista_qt(self, value):

        from front_end.menor import Menor

        class_menor = Menor()
        if value:  # Verifica se a string está vazia
            if value != "":
                try:
                    quantidade = int(value)  # Tenta converter para inteiro

                    if quantidade < 1:

                        class_menor.snack_bar_floating_button(
                            "Formato inválido, digite número positivo"
                        )
                    elif quantidade > 0:

                        ButtonSheetAdicionar.lista_if_adic["quantidade"] = quantidade

                except ValueError:

                    class_menor.snack_bar_floating_button(
                        "Formato inválido, digite número positivo"
                    )

    def salvar_historico(self, entrada):

        from front_end.menor import Menor
        from front_exe import Pagina

        class_menor_1 = Menor()

        if ButtonSheetAdicionar.lista_if_adic["produto"] == "" or (
            ButtonSheetAdicionar.lista_if_adic["quantidade"] == ""
        ):

            class_menor_1.snack_bar_floating_button(
                "adicione o produto e quantidade"
            )

        elif ButtonSheetAdicionar.lista_if_adic["produto"] != "" and (
            ButtonSheetAdicionar.lista_if_adic["quantidade"] != ""
        ):

            if ButtonSheetAdicionar.lista_if_adic["subproduto"] != "":

                var_len = self.sheadic_select_query_dupla__len_subp(
                    entrada,
                    ButtonSheetAdicionar.lista_if_adic["produto"],
                    ButtonSheetAdicionar.lista_if_adic["subproduto"]

                )

                if len(var_len) == 0:

                    self.sheadic_insert_query_tripla(
                        entrada,
                        ButtonSheetAdicionar.lista_if_adic["produto"],
                        ButtonSheetAdicionar.lista_if_adic["subproduto"],
                        ButtonSheetAdicionar.lista_if_adic["quantidade"]
                    )

                    self.limpar_lista_classe()

                    if self.bs:
                        self.bs.open = False
                        Pagina.PAGE.update()

                elif len(var_len) > 0:

                    class_menor_1.snack_bar_floating_button(
                        "Está na lista."
                    )
            elif ButtonSheetAdicionar.lista_if_adic["subproduto"] == "":

                var_lista = self.sheadic_select_listaquery_subentrada(
                    ButtonSheetAdicionar.lista_if_adic["produto"]
                )
                if len(var_lista) == 0:

                    var_len_1 = self.sheadic_select_query_dupla__len_s_subp(
                        entrada,
                        ButtonSheetAdicionar.lista_if_adic["produto"]

                    )
                    if len(var_len_1) == 0:
                        self.sheadic_insert_query_tripla(
                            entrada,
                            ButtonSheetAdicionar.lista_if_adic["produto"],
                            ButtonSheetAdicionar.lista_if_adic["subproduto"],
                            ButtonSheetAdicionar.lista_if_adic["quantidade"]
                        )

                        self.limpar_lista_classe()

                        if self.bs:
                            self.bs.open = False
                            Pagina.PAGE.update()

                    elif len(var_len_1) > 0:

                        class_menor_1.snack_bar_floating_button(
                            "Está na lista."
                        )
                elif len(var_lista) != 0:

                    class_menor_1.snack_bar_floating_button(
                        "Subproduto não adicionado."
                    )

    def adicionar_itens_lista(self, data):
        return Column(
            controls=[
                Column(
                    controls=[
                        Text(value="Produto:", size=16),
                        Container(
                            content=AutoComplete(
                                suggestions=self.sheadic_select_lista_entrada(),
                                on_select=lambda e: self.atualizar_subprodutos(
                                    e.control.suggestions[e.control.selected_index].key,
                                    e.control.suggestions[e.control.selected_index].value
                                ),


                            ),
                            expand=True,
                        ),
                    ]
                ),
                Column(
                    controls=[
                        Dropdown(
                            ref=self.dropdown_ref_adic,  # Associa a referência ao Dropdown
                            expand=True,
                            options=[],
                            on_change=lambda e: self.lista_subproduto_adic_dropdawn(
                                e.control.value)
                        )
                    ]
                ),
                TextField(
                    adaptive=True,
                    label="Quantidade:",
                    on_change=lambda e: self.lista_qt(
                        e.control.value)),
                Row([
                    FilledButton(
                        "Cancelar",
                        on_click=self.close_bottom_sheet,
                    ),
                    FilledButton(
                        "Aplicar",
                        on_click=lambda e: self.salvar_historico(data)
                    ),
                ])
            ]
        )

    def close_bottom_sheet(self, e):
        from front_exe import Pagina
        if self.bs:
            self.bs.open = False
            Pagina.PAGE.update()

    def ativar_item(self, data):
        from front_exe import Pagina

        self.bs = BottomSheet(
            open=True,
            content=Container(
                padding=20,
                content=Column(
                    controls=[
                        self.adicionar_itens_lista(data[0]),
                    ]
                ),
            ),
        )
        Pagina.PAGE.overlay.append(self.bs)
        Pagina.PAGE.update()

    def limpar_lista_classe(self):

        ButtonSheetAdicionar.lista_if_adic["produto"] = ""
        ButtonSheetAdicionar.lista_if_adic["subproduto"] = ""
        ButtonSheetAdicionar.lista_if_adic["quantidade"] = ""
