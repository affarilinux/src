
from flet import FloatingActionButton, Icons, SnackBar, Text, FontWeight

import flet as ft


class Loja:

    def lj_criar_panellist(self):

        from front_exe import Pagina

        panel = ft.ExpansionPanelList(
            expand_icon_color=ft.Colors.AMBER,
            elevation=8,
            divider_color=ft.Colors.AMBER,
            # on_change=handle_change,
            controls=[
                ft.ExpansionPanel(
                    # has no header and content - placeholders will be used
                    bgcolor=ft.Colors.BLUE_400,
                    expanded=True,
                )
            ]
        )

        colors = [
            ft.Colors.GREEN_500,
            ft.Colors.BLUE_800,
            ft.Colors.RED_800,
        ]

        for i in range(10):
            exp = ft.ExpansionPanel(
                bgcolor=colors[i % len(colors)],
                header=ft.ListTile(title=ft.Text(f"Panel {i}")),
            )

            exp.content = ft.ListTile(
                title=ft.Text(f"This is in Panel {i}"),
                subtitle=ft.Text(f"Press the icon to delete panel {i}"),
                trailing=ft.IconButton(
                    ft.Icons.DELETE,
                    # on_click=handle_delete,
                    data=exp),
            )

            panel.controls.append(exp)

        Pagina.PAGE.add(panel)

    def lj_criar_button_lista(self):

        from front_exe import Pagina

        def salvar_banco(e):

            Pagina.PAGE.open(SnackBar(Text(
                "{} Salvo.".format("tenda"),
                color="#4F4F4F",  # Grey
                size=20,
                weight=FontWeight.W_900
            )))

        Pagina.PAGE.floating_action_button = FloatingActionButton(
            icon=Icons.ADD,
            on_click=salvar_banco,
            bgcolor="#FFFF00",  # Yellow
            foreground_color="#4F4F4F"  # Grey # color
        )

    def lj_criar_pagina(self):

        from front_exe import Pagina

        self.lj_criar_panellist()

        self.lj_criar_button_lista()

        Pagina.PAGE.update()

    def lj_remover_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.floating_action_button = None

        Pagina.PAGE.update()
