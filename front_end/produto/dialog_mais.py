
from flet import (SnackBar, Text, FontWeight, TextField, TextButton,
                  AlertDialog, Text
                  )


class DialogMais:

    def dialogo_produto(self):

        from front_exe import Pagina

        def Cancelar(e):

            Pagina.PAGE.close(self.dialog_pd)  # Fecha o diálogo
            Pagina.PAGE.update()

        def aplicar_dados(e):

            self.dialogo_execucao(dialog_textfield.value)

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
        self.dialog_pd = AlertDialog(
            title=Text("Digite o nome:"),
            content=dialog_textfield,  # primaria
            actions=material_actions,  # secundaria
        )

        Pagina.PAGE.open(self.dialog_pd)

        Pagina.PAGE.update()

    def dialogo_execucao(self, nome):

        from front_exe import Pagina

        if nome != "":

            var_lista_nome = self.pddb_selecionar_nome()

            if nome not in var_lista_nome:

                self.pddb_inserir_nome_contagem(nome)

                self.snack_bar_floating_button("{} salvo.".format(nome))

                Pagina.PAGE.remove(self.list_view_pd)
                Pagina.PAGE.update()

                self.pd_criar_panellist(
                    self.lista_produto_sqlite_produto()
                )
                Pagina.PAGE.update()

                Pagina.PAGE.close(self.dialog_pd)  # Fecha o diálogo
                Pagina.PAGE.update()

            elif nome in var_lista_nome:

                self.snack_bar_floating_button(
                    "escreva outro nome: {}".format(nome))

    def snack_bar_floating_button(self, frase):

        from front_exe import Pagina

        Pagina.PAGE.open(SnackBar(Text(
            frase,
            color="#4F4F4F",  # Grey
            size=20,
            weight=FontWeight.W_900
        )))
