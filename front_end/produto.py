from flet import (FloatingActionButton, Icons, SnackBar, Text, FontWeight, ListView
                  )
import flet as ft


class produto:

    def pd_criar_panellist(self):

        from front_exe import Pagina

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

    def pd_criar_button_lista(self):

        from front_exe import Pagina

        def salvar_banco(e):

            Pagina.PAGE.open(SnackBar(Text(  # barra inferior
                "{} Salvo.".format("tenda"),
                color="#4F4F4F",  # Grey
                size=20,
                weight=FontWeight.W_900
            )))

        Pagina.PAGE.floating_action_button = FloatingActionButton(
            icon=Icons.ADD,
            on_click=salvar_banco,
            bgcolor="#FFFF00",  # Yellow
            foreground_color="#4F4F4F",  # Grey color
            visible=True  # Define inicialmente visível
        )

    def pd_criar_pagina(self):

        from front_exe import Pagina

        self.pd_criar_panellist()
        self.pd_criar_button_lista()
        Pagina.PAGE.update()

    def pd_remover_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.floating_action_button = None
        Pagina.PAGE.update()
