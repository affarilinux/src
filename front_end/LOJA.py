
from flet import (FloatingActionButton, Icons, SnackBar, Text, FontWeight, ListView
                  )
import flet as ft


class Loja:

    def lj_criar_panellist(self):
        from front_exe import Pagina

        """panel = ft.ExpansionPanelList(
            expand_icon_color=ft.Colors.AMBER,
            elevation=8,
            divider_color=ft.Colors.AMBER,

        )

        colors = [
            ft.Colors.GREEN_500,
            ft.Colors.BLUE_800,
            ft.Colors.RED_800,
        ]

        for i in range(30):
            exp = ft.ExpansionPanel(
                bgcolor=colors[i % len(colors)],
                header=ft.ListTile(title=ft.Text(f"Panel {i}")),
            )

            exp.content = ft.ListTile(
                title=ft.Text(f"This is in Panel {i}"),
                subtitle=ft.Text(f"Press the icon to delete panel {i}"),
                trailing=ft.IconButton(
                    ft.Icons.DELETE,
                    data=exp),
            )

            panel.controls.append(exp)"""

        panel = ft.ExpansionPanelList(
            expand_icon_color=ft.Colors.AMBER,
            elevation=8,
            divider_color=ft.Colors.AMBER,

        )

        colors = [
            ft.Colors.GREEN_500,
            ft.Colors.BLUE_800,
            ft.Colors.RED_800,
        ]

        for i in range(30):
            exp = ft.ExpansionPanel(
                bgcolor=colors[i % len(colors)],
                header=ft.ListTile(title=ft.Text(f"Panel {i}")),
            )

            # Adicionando múltiplos IconButtons no conteúdo
            exp.content = ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(
                                ft.Icons.EDIT,
                                tooltip="Edit",
                                # on_click=handle_edit,
                                data=i,
                            ),
                            ft.IconButton(
                                ft.Icons.DELETE,
                                tooltip="Delete",
                                # on_click=handle_delete,
                                data=exp,
                            ),
                            ft.IconButton(
                                ft.Icons.SHARE,
                                tooltip="Share",
                                # on_click=handle_share,
                                data=i,
                            ),
                        ],
                        alignment="start",
                    ),
                ]
            )

            panel.controls.append(exp)

        def handle_scroll(e):

            # Desaparecer o botão imediatamente quando rolar para baixo
            if e.scroll_delta is not None:

                if e.scroll_delta > 0:  # rola para baixo

                    Pagina.PAGE.floating_action_button.visible = False
                    Pagina.PAGE.update()

                elif e.scroll_delta < 0:  # rola para cima

                    Pagina.PAGE.floating_action_button.visible = True
                    Pagina.PAGE.update()

        list_view = ListView(
            expand=True,
            spacing=10,
            padding=10,
            controls=[panel],
            on_scroll=handle_scroll,
        )

        Pagina.PAGE.add(list_view)

    def lj_criar_button_lista(self):
        from front_exe import Pagina

        def salvar_banco(e):
            self.dialogo_sqlite()

        Pagina.PAGE.floating_action_button = FloatingActionButton(
            icon=Icons.ADD,
            on_click=salvar_banco,
            bgcolor="#FFFF00",  # Yellow
            foreground_color="#4F4F4F",  # Grey color
            visible=True  # Define inicialmente visível
        )

    def dialogo_sqlite(self):

        from front_exe import Pagina

        # Campo de entrada no diálogo
        dialog_textfield = ft.TextField(label="Digite algo:", expand=True)

        material_actions = [
            ft.TextButton(text="Yes",  # on_click=handle_action_click
                          ),
            ft.TextButton(text="No",  # on_click=handle_action_click
                          ),

        ]
        dialog = ft.AlertDialog(
            title=ft.Text("Digite o nome:"),
            content=dialog_textfield,  # primaria
            actions=material_actions,  # secundaria
        )

        Pagina.PAGE.open(dialog)

        Pagina.PAGE.update()

    def snack_bar_floating_button(self):

        from front_exe import Pagina

        Pagina.PAGE.open(SnackBar(Text(
            "{} Salvo.".format("tenda"),
            color="#4F4F4F",  # Grey
            size=20,
            weight=FontWeight.W_900
        )))

    def lj_criar_pagina(self):

        from front_exe import Pagina

        self.lj_criar_panellist()
        self.lj_criar_button_lista()
        Pagina.PAGE.update()

    def lj_remover_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.floating_action_button = None
        Pagina.PAGE.update()
