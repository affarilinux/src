from flet import (SnackBar, Text, FontWeight, TextField, TextButton,
                  AlertDialog
                  )


class EditarNome:

    def dialogo_editar_produto(self, titulo):

        from front_exe import Pagina

        def cancelar_editar(e):

            Pagina.PAGE.close(self.pd_dialog)  # Fecha o diálogo
            Pagina.PAGE.update()

        def aplicar_editar(e):

            self.dialogo_execucao_editar(pd_dialog_textfield.value, titulo)

        pd_dialog_textfield = TextField(label="Editar nome:", expand=True)

        pd_material_actions = [
            TextButton(
                text="Cancelar",
                on_click=cancelar_editar
            ),
            TextButton(
                text="Aplicar",
                on_click=aplicar_editar
            ),

        ]
        self.pd_dialog = AlertDialog(
            title=Text("Digite o nome:"),
            content=pd_dialog_textfield,  # primaria
            actions=pd_material_actions,  # secundaria
        )

        Pagina.PAGE.open(self.pd_dialog)

        Pagina.PAGE.update()

    def dialogo_execucao_editar(self, nome, titulo):

        from front_exe import Pagina

        if nome != "":

            var_lista_nome = self.pddb_selecionar_nome()

            if nome not in var_lista_nome:

                var_num = self.pddb_selecionar_index_nome(titulo)

                self.pddb_editar_nome(nome, var_num)

                self.snack_bar_floating_button("{} salvo.".format(nome))

                Pagina.PAGE.remove(self.list_view_pd)
                Pagina.PAGE.update()

                self.pd_criar_panellist()
                Pagina.PAGE.update()

                Pagina.PAGE.close(self.pd_dialog)  # Fecha o diálogo
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
