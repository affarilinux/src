
from flet import (Text, TextField, TextButton,
                  AlertDialog, Text
                  )


class DialogMaisLista:

    def dialogo_entrada(self):

        from front_exe import Pagina

        def Cancelar(e):

            Pagina.PAGE.close(self.dialog_lista)  # Fecha o diálogo
            Pagina.PAGE.update()

        def aplicar_dados(e):

            self.dm_dialogo_execucao(dialog_textfield.value)

            # Campo de entrada no diálogo
        dialog_textfield = TextField(label="Digite algo:", expand=True)

        material_actions = [
            TextButton(
                text="Cancelar",
                on_click=Cancelar
            ),
            TextButton(
                text="Aplicar",
                on_click=aplicar_dados
            ),

        ]
        self.dialog_lista = AlertDialog(
            title=Text("Digite o nome:"),
            content=dialog_textfield,  # primaria
            actions=material_actions,  # secundaria
        )

        Pagina.PAGE.open(self.dialog_lista)

        Pagina.PAGE.update()

    def dm_dialogo_execucao(self, nome):

        from front_exe import Pagina
        from front_end.menor import Menor

        class_menor = Menor()

        if nome != "":

            var_lista_nome = self.et_selecionar_nome()

            if nome not in var_lista_nome:

                self.et_inserir_nome_contagem(nome)

                class_menor.snack_bar_floating_button(
                    "{} salvo.".format(nome)
                )

                Pagina.PAGE.remove(self.list_view_ent)
                Pagina.PAGE.update()

                self.pd_criar_panellist(
                    self.lista_entrada_sqlite()
                )
                Pagina.PAGE.update()

                Pagina.PAGE.close(self.dialog_pd)  # Fecha o diálogo
                Pagina.PAGE.update()

            elif nome in var_lista_nome:

                class_menor.snack_bar_floating_button(
                    "escreva outro nome: {}".format(nome)
                )
