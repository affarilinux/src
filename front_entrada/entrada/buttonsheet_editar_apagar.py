
from flet import (Column, Container,
                  TextField, FilledButton, BottomSheet, Row,
                  Dropdown, Ref)


from front_entrada.entrada.db.bs_editar_apagar import (dbBSEditar)


class ButtonSheetEditar(dbBSEditar):

    lista_subproduto_adit = []
    dropdown_ref_edit = Ref[Dropdown]()  # Adiciona uma referência ao Dropdown

    lista_if_edit = {
        "produto": "", "subproduto": "", "quantidade": ""
    }

    lista_if_edit_2 = {
        "subproduto": "", "quantidade": ""
    }

    def atualizar_subprodutos_editar(self):

        from front_exe import Pagina
        from flet import dropdown

        # Obter os subprodutos com base no produto selecionado
        subprodutos = self.bse_select_query_lista(
            ButtonSheetEditar.lista_if_edit["produto"])

        # Converter a lista de strings em uma lista de Dropdown.Option
        self.dropdown_ref_edit.current.options = [
            dropdown.Option(key=item, text=item) for item in subprodutos
        ]

        # Atualizar o Dropdown na interface
        self.dropdown_ref_edit.current.update()

        Pagina.PAGE.update()

    def lista_subproduto_adit_dropdawn_editar(self, value):

        if value != "":

            if value != ButtonSheetEditar.lista_if_edit["subproduto"]:
                ButtonSheetEditar.lista_if_edit_2["subproduto"] = value

            elif value == ButtonSheetEditar.lista_if_edit["subproduto"]:
                ButtonSheetEditar.lista_if_edit_2["subproduto"] = ""

    def lista_quantidade(self, value):

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

                        if quantidade != ButtonSheetEditar.lista_if_edit["quantidade"]:
                            ButtonSheetEditar.lista_if_edit_2["quantidade"] = quantidade

                        elif quantidade == ButtonSheetEditar.lista_if_edit["quantidade"]:

                            ButtonSheetEditar.lista_if_edit_2["quantidade"] = ""
                except ValueError:

                    class_menor.snack_bar_floating_button(
                        "Formato inválido, digite número positivo"
                    )

    def salvar_historico_editar(self, entrada):

        print(ButtonSheetEditar.lista_if_edit)
        print(ButtonSheetEditar.lista_if_edit_2)

        if ButtonSheetEditar.lista_if_edit_2["subproduto"] == "" and (
            ButtonSheetEditar.lista_if_edit_2["quantidade"] == ""
        ):

            from front_end.menor import Menor

            class_menor_1 = Menor()

            class_menor_1.snack_bar_floating_button(
                "ecolha subproduto e quantidade"
            )

        else:
            print(123)

        """if ButtonSheetEditar.lista_if_edit["produto"] == "" or (
            ButtonSheetEditar.lista_if_edit["quantidade"] == ""
        ):

            from front_end.menor import Menor

            class_menor_1 = Menor()

            class_menor_1.snack_bar_floating_button(
                "adicione o produto e quantidade"
            )

        elif ButtonSheetEditar.lista_if_edit["produto"] != "" and (
            ButtonSheetEditar.lista_if_edit["quantidade"] != ""
        ):

            self.sheadic_insert_query_tripla(
                entrada,
                ButtonSheetEditar.lista_if_edit["produto"],
                ButtonSheetEditar.lista_if_edit["subproduto"],
                ButtonSheetEditar.lista_if_edit["quantidade"]
            )
            self.limpar_lista_classe()

            from front_exe import Pagina
            if self.bs:
                self.bs.open = False
                Pagina.PAGE.update()"""

    def adicionar_itens_lista_editar(self, data):
        return Column(
            controls=[

                Column(
                    controls=[
                        Dropdown(
                            ref=self.dropdown_ref_edit,  # Associa a referência ao Dropdown
                            expand=True,
                            options=[],
                            on_change=lambda e: self.lista_subproduto_adit_dropdawn_editar(
                                e.control.value)
                        )
                    ]
                ),
                TextField(
                    adaptive=True,
                    label="Quantidade:",
                    on_change=lambda e: self.lista_quantidade(
                        e.control.value)),
                Row([
                    FilledButton(
                        "Cancelar",
                        on_click=self.close_bottom_sheet,
                    ),
                    FilledButton(
                        "Aplicar",
                        on_click=lambda e: self.salvar_historico_editar(data)
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

        ButtonSheetEditar.lista_if_edit["produto"] = ""
        ButtonSheetEditar.lista_if_edit["subproduto"] = ""
        ButtonSheetEditar.lista_if_edit["quantidade"] = ""
