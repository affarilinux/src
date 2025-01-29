
from flet import (Text, TextField, TextButton, IconButton, Icons,
                  AlertDialog, Text
                  )

from front_entrada.entrada.db.dialog_edit_apag_db import dbDialogeditApagar


class DialogEditarApagar(dbDialogeditApagar):

    lista_if_edit = {
        "entrada": "", "produto": "", "subproduto": "", "quantidade": ""
    }

    def dialogo_subentrada(self):

        from front_exe import Pagina

        def Cancelar(e):

            Pagina.PAGE.close(self.dialog_pd)  # Fecha o diálogo
            Pagina.PAGE.update()

            # Campo de entrada no diálogo
        dialog_textfield = TextField(label="Digite número:", expand=True)

        material_actions = [
            IconButton(
                Icons.DELETE,
                tooltip="Deletar",
                on_click=lambda e: self.deletar_linha_subentrada()
            ),
            TextButton(
                text="Cancelar",
                on_click=Cancelar
            ),
            TextButton(
                text="Aplicar",
                on_click=lambda e: self.dea_dialogo_execucao(
                    dialog_textfield.value)
            ),

        ]
        self.dialog_pd = AlertDialog(
            title=Text("Digite um número:"),
            content=dialog_textfield,  # primaria
            actions=material_actions,  # secundaria
        )

        Pagina.PAGE.open(self.dialog_pd)

        Pagina.PAGE.update()

    def deletar_linha_subentrada(self):

        from front_exe import Pagina
        from front_end.menor import Menor

        class_menor = Menor()

        if DialogEditarApagar.lista_if_edit["subproduto"] != (
                "*S/subproduto"):
            self.dbdea_delete_subentrada_trilo(
                DialogEditarApagar.lista_if_edit["entrada"],
                DialogEditarApagar.lista_if_edit["produto"],
                DialogEditarApagar.lista_if_edit["subproduto"]
            )
        elif DialogEditarApagar.lista_if_edit["subproduto"] == (
                "*S/subproduto"):
            self.dbdea_delete_subentrada_duplo(
                DialogEditarApagar.lista_if_edit["entrada"],
                DialogEditarApagar.lista_if_edit["produto"]
            )

        class_menor.snack_bar_floating_button(
            "Deletado {}.".format(
                DialogEditarApagar.lista_if_edit["produto"]
            )
        )

        Pagina.PAGE.remove(self.list_view_ent)
        Pagina.PAGE.update()

        self.pd_criar_panellist(
            self.lista_entrada_sqlite()
        )
        Pagina.PAGE.update()

        Pagina.PAGE.close(self.dialog_pd)  # Fecha o diálogo
        Pagina.PAGE.update()

    def dea_dialogo_execucao(self, numero):

        from front_exe import Pagina
        from front_end.menor import Menor

        class_menor = Menor()

        if numero != "":

            if numero != DialogEditarApagar.lista_if_edit["quantidade"]:

                if DialogEditarApagar.lista_if_edit["subproduto"] != (
                        "*S/subproduto"):

                    self.dbdea_update_mumero_subentrada_trilo(
                        DialogEditarApagar.lista_if_edit["entrada"],
                        DialogEditarApagar.lista_if_edit["produto"],
                        DialogEditarApagar.lista_if_edit["subproduto"],
                        numero
                    )

                elif DialogEditarApagar.lista_if_edit["subproduto"] == (
                        "*S/subproduto"):

                    self.dbdea_update_mumero_subentrada_dupla(
                        DialogEditarApagar.lista_if_edit["entrada"],
                        DialogEditarApagar.lista_if_edit["produto"],
                        numero
                    )

                class_menor.snack_bar_floating_button(
                    "{} salvo.".format(numero)
                )

                Pagina.PAGE.remove(self.list_view_ent)
                Pagina.PAGE.update()

                self.pd_criar_panellist(
                    self.lista_entrada_sqlite()
                )
                Pagina.PAGE.update()

                Pagina.PAGE.close(self.dialog_pd)  # Fecha o diálogo
                Pagina.PAGE.update()
            elif numero == DialogEditarApagar.lista_if_edit["quantidade"]:

                class_menor.snack_bar_floating_button(
                    "escreva outro número: {}".format(numero)
                )
