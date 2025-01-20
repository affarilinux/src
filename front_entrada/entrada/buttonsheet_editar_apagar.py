
from flet import (Column, Container,
                  TextField, FilledButton, BottomSheet, Row,
                  Dropdown, Ref)

from front_entrada.entrada.db.subentreda_btsheet_adicionar import (
    SubEntradaBtsheetAdicionarDB)
from front_entrada.entrada.db.bs_editar_apagar import (dbBSEditar)


class ButtonSheetEditar(SubEntradaBtsheetAdicionarDB, dbBSEditar):

    lista_subproduto = []
    dropdown_ref = Ref[Dropdown]()  # Adiciona uma referência ao Dropdown

    lista_if = {
        "produto": "", "subproduto": "", "quantidade": ""
    }

    def atualizar_subprodutos_editar(self):

        from front_exe import Pagina

        print(self.bse_select_query_lista(
            ButtonSheetEditar.lista_if["produto"]
        ))

        self.dropdown_ref.current.options = self.bse_select_query_lista(
            ButtonSheetEditar.lista_if["produto"]
        )

        self.dropdown_ref.current.update()  # Força a atualização do Dropdown

        Pagina.PAGE.update()
        """from front_exe import Pagina

        # Atualiza a lista de subprodutos
        ButtonSheetEditar.lista_subproduto = (
            self.sheadic_select_listaquery_subentrada(produto)
        )

        # Cria as opções do Dropdown a partir da lista de strings
        self.dropdown_ref.current.options = [
            dropdown.Option(key=item, text=item) for item in ButtonSheetEditar.lista_subproduto
        ]
        self.dropdown_ref.current.update()  # Força a atualização do Dropdown

        ButtonSheetEditar.lista_if["produto"] = selecao
        ButtonSheetEditar.lista_if["subproduto"] = ""

        Pagina.PAGE.update()"""

    def lista_subproduto_dropdawn(self, value):

        if value != "":

            ButtonSheetEditar.lista_if["subproduto"] = value

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

                        ButtonSheetEditar.lista_if["quantidade"] = quantidade

                except ValueError:

                    class_menor.snack_bar_floating_button(
                        "Formato inválido, digite número positivo"
                    )

    def salvar_historico(self, entrada):

        if ButtonSheetEditar.lista_if["produto"] == "" or (
            ButtonSheetEditar.lista_if["quantidade"] == ""
        ):

            from front_end.menor import Menor

            class_menor_1 = Menor()

            class_menor_1.snack_bar_floating_button(
                "adicione o produto e quantidade"
            )

        elif ButtonSheetEditar.lista_if["produto"] != "" and (
            ButtonSheetEditar.lista_if["quantidade"] != ""
        ):

            self.sheadic_insert_query_tripla(
                entrada,
                ButtonSheetEditar.lista_if["produto"],
                ButtonSheetEditar.lista_if["subproduto"],
                ButtonSheetEditar.lista_if["quantidade"]
            )
            self.limpar_lista_classe()

            from front_exe import Pagina
            if self.bs:
                self.bs.open = False
                Pagina.PAGE.update()

    def adicionar_itens_lista_editar(self, data):
        return Column(
            controls=[

                Column(
                    controls=[
                        Dropdown(
                            ref=self.dropdown_ref,  # Associa a referência ao Dropdown
                            expand=True,
                            options=[],
                            on_change=lambda e: self.lista_subproduto_dropdawn(
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

    def ativar_item_editar(self, data):
        from front_exe import Pagina

        self.bs = BottomSheet(
            open=True,
            content=Container(
                padding=20,
                content=Column(
                    controls=[
                        self.adicionar_itens_lista_editar(data[0]),
                    ]
                ),
            ),
        )
        Pagina.PAGE.overlay.append(self.bs)

        Pagina.PAGE.update()

        # fazer o update depois atualizar dropdawn
        self.atualizar_subprodutos_editar()

    def limpar_lista_classe(self):

        ButtonSheetEditar.lista_if["produto"] = ""
        ButtonSheetEditar.lista_if["subproduto"] = ""
        ButtonSheetEditar.lista_if["quantidade"] = ""
