

from flet import (Text, TextField, TextButton,
                  AlertDialog, Text, IconButton, Icons
                  )

from front_configuracao.produto.db.dialog_SP_editar import (
    DBDialogSPEditar
)


class DialogSubProdutoEditar(DBDialogSPEditar):

    def dialogo_subproduto_editar(self, produtonome, sublista):

        from front_exe import Pagina

        def Cancelar(e):

            Pagina.PAGE.close(self.dialog_pd)  # Fecha o diálogo
            Pagina.PAGE.update()

            # Campo de entrada no diálogo
        dialog_textfield = TextField(label="Digite algo:", expand=True)

        material_actions = [
            IconButton(
                Icons.DELETE,
                tooltip="Deletar",
                data=sublista,
                on_click=lambda e: self.apagar_sublista(
                    produtonome, e.control.data)
            ),

            TextButton(
                text="Cancelar",
                on_click=Cancelar
            ),
            TextButton(
                text="Aplicar",
                on_click=lambda e: self.editar_dialogo_execucao(
                    dialog_textfield.value, produtonome, sublista)
            ),

        ]
        self.dialog_pd = AlertDialog(
            title=Text("Editar lista:"),
            content=dialog_textfield,  # primaria
            actions=material_actions,  # secundaria
        )

        Pagina.PAGE.open(self.dialog_pd)

        Pagina.PAGE.update()

    def editar_dialogo_execucao(self, nome, produtonome, sublista):

        from front_exe import Pagina
        from front_end.menor import Menor

        class_menor = Menor()

        if nome != "":

            var_status = self.subpro_queryrepetido(produtonome, nome)

            if var_status == False:

                self.diaedit_editar_nome(
                    nome,
                    self.diaedit_selecionar_index_nome_produto(produtonome),
                    self.diaedit_selecionar_index_subnome_subproduto(sublista))

                class_menor.snack_bar_floating_button(
                    "{} salvo.".format(nome)
                )

                Pagina.PAGE.remove(self.list_view_pd)
                Pagina.PAGE.update()

                self.pd_criar_panellist(
                    self.lista_produto_sqlite_produto()
                )
                Pagina.PAGE.update()

                Pagina.PAGE.close(self.dialog_pd)  # Fecha o diálogo
                Pagina.PAGE.update()

            elif var_status == True:

                class_menor.snack_bar_floating_button(
                    "escreva outro nome: {}".format(nome))

    def apagar_sublista(self, produtonome, sublista):

        from front_exe import Pagina
        from front_end.menor import Menor

        class_menor_ap = Menor()

        self.diaedit_deletar_nome(
            self.diaedit_selecionar_index_nome_produto(produtonome),
            self.diaedit_selecionar_index_subnome_subproduto(sublista))

        class_menor_ap.snack_bar_floating_button(
            "{} apagado.".format(sublista)
        )

        Pagina.PAGE.remove(self.list_view_pd)
        Pagina.PAGE.update()

        self.pd_criar_panellist(
            self.lista_produto_sqlite_produto()
        )
        Pagina.PAGE.update()

        Pagina.PAGE.close(self.dialog_pd)  # Fecha o diálogo
        Pagina.PAGE.update()
