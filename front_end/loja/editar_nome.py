import flet as ft


class EditarNome:

    def dialogo_editar(self):

        from front_exe import Pagina

        dialog_textfield = ft.TextField(label="Editar nome:", expand=True)

        material_actions = [
            ft.TextButton(
                text="Cancelar",
                # on_click=Cancelar
            ),
            ft.TextButton(
                text="Aplicar",
                # on_click=aplicar_dados
            ),

        ]
        self.dialog = ft.AlertDialog(
            title=ft.Text("Digite o nome:"),
            content=dialog_textfield,  # primaria
            actions=material_actions,  # secundaria
        )

        Pagina.PAGE.open(self.dialog)

        Pagina.PAGE.update()
