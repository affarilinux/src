from flet import (Text, TextField, TextButton,
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
            title=Text("Atualize o nome:"),
            content=pd_dialog_textfield,  # primaria
            actions=pd_material_actions,  # secundaria
        )

        Pagina.PAGE.open(self.pd_dialog)

        Pagina.PAGE.update()

    def dialogo_execucao_editar(self, nome, titulo):

        from front_exe import Pagina
        from front_end.menor import Menor

        class_menor = Menor()

        if nome != "":

            var_lista_nome = self.et_selecionar_nome()

            if nome not in var_lista_nome:

                var_num = self.et_selecionar_index_nome(titulo)

                self.et_editar_nome(nome, var_num)

                class_menor.snack_bar_floating_button(
                    "{} salvo.".format(nome)
                )

                Pagina.PAGE.remove(self.list_view_ent)
                Pagina.PAGE.update()

                self.pd_criar_panellist(
                    self.lista_entrada_sqlite()
                )
                Pagina.PAGE.update()

                Pagina.PAGE.close(self.pd_dialog)  # Fecha o diálogo
                Pagina.PAGE.update()

            elif nome in var_lista_nome:

                class_menor.snack_bar_floating_button(
                    "escreva outro nome: {}".format(nome)
                )
