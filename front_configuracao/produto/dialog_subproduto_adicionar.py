
from flet import (Text, TextField, TextButton,
                  AlertDialog, Text
                  )

from front_configuracao.produto.db.subproduto_dialog_subprod_adic import (
    SubprodutoDialogSubprodutoAdicionar
)


class DialogSubProdutoAdicionar(SubprodutoDialogSubprodutoAdicionar):

    def dialogo_subproduto(self, produtonome):

        from front_exe import Pagina

        def Cancelar(e):

            Pagina.PAGE.close(self.dialog_pd)  # Fecha o diálogo
            Pagina.PAGE.update()

            # Campo de entrada no diálogo
        dialog_textfield = TextField(label="Digite algo:", expand=True)

        material_actions = [
            TextButton(
                text="Cancelar",
                on_click=Cancelar
            ),
            TextButton(
                text="Aplicar",
                on_click=lambda e: self.subp_dialogo_execucao(
                    dialog_textfield.value, produtonome[0])
            ),

        ]
        self.dialog_pd = AlertDialog(
            title=Text("Adicionar lista:"),
            content=dialog_textfield,  # primaria
            actions=material_actions,  # secundaria
        )

        Pagina.PAGE.open(self.dialog_pd)

        Pagina.PAGE.update()

    def subp_dialogo_execucao(self, nome, produtonome):

        from front_exe import Pagina
        from front_end.menor import Menor

        class_menor = Menor()

        if nome != "":

            var_status = self.subpro_queryrepetido(produtonome, nome)

            if var_status == False:

                self.subpro_inserir_nome_subproduto(
                    self.subpro_selecionar_index_nome_produto(produtonome),
                    nome
                )

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
