
from flet import (FloatingActionButton, Icons, SnackBar, Text,
                  FontWeight, ListView, Colors
                  )
import flet as ft

from banco_sqlite.loja import LojaDB


class Loja:

    def __init__(self):

        self.lojadb = LojaDB()

    def lj_criar_panellist(self):
        from front_exe import Pagina

        def editar_lista(e):

            self.dialogo_editar()

        varlist_loja = self.lojadb.selecionar_nome_contagem()

        # Lista de cores para os painéis
        colors = [
            "#00FF7F",  # SpringGreen
            "#20B2AA",  # LightSeaGreen
            "#708090",  # SlateGray
            "#B8860B",  # DarkGoldenrod
            "#4B0082"  # Indigo

        ]

        # Lista para armazenar os painéis
        panels = []

        # Criando os painéis no loop
        for i, loja_nome in enumerate(varlist_loja):
            exp = ft.ExpansionPanel(
                bgcolor=colors[i % len(colors)],
                header=ft.ListTile(
                    title=ft.Text(f" {loja_nome[0]}")
                ),
            )

            # Adicionando múltiplos IconButtons no conteúdo
            exp.content = ft.Column(
                [
                    ft.Row(
                        [
                            ft.IconButton(
                                ft.Icons.EDIT,
                                tooltip="Editar",
                                data=loja_nome,
                                on_click=editar_lista
                            ),
                            ft.IconButton(
                                ft.Icons.DELETE,
                                tooltip="Deletar",
                                data=loja_nome,
                            ),

                        ],
                        alignment="start",
                    ),
                ]
            )

            # Adiciona o painel à lista de painéis
            panels.append(exp)

        panel = ft.ExpansionPanelList(
            expand_icon_color=ft.Colors.AMBER,
            elevation=8,
            divider_color=ft.Colors.AMBER,
            controls=panels

        )
        # ****************************************
        # rolo da lista

        def handle_scroll(e):

            # Desaparecer o botão imediatamente quando rolar para baixo
            if e.scroll_delta is not None:

                if e.scroll_delta > 0:  # rola para baixo

                    Pagina.PAGE.floating_action_button.visible = False
                    Pagina.PAGE.update()

                elif e.scroll_delta < 0:  # rola para cima

                    Pagina.PAGE.floating_action_button.visible = True
                    Pagina.PAGE.update()

        self.list_view = ListView(
            expand=True,
            spacing=10,
            padding=10,
            controls=[panel],
            on_scroll=handle_scroll,
        )

        Pagina.PAGE.add(self.list_view)

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

    ##############################################
    # butao mais

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
    # ****************************************
    # alertdialog inserir

    def dialogo_sqlite(self):

        from front_exe import Pagina

        def Cancelar(e):

            Pagina.PAGE.close(self.dialog)  # Fecha o diálogo
            Pagina.PAGE.update()

        def aplicar_dados(e):

            self.alertdialog_banco_inserir(dialog_textfield.value)

            # Campo de entrada no diálogo
        dialog_textfield = ft.TextField(label="Digite algo:", expand=True)

        material_actions = [
            ft.TextButton(
                text="Cancelar",
                on_click=Cancelar
            ),
            ft.TextButton(
                text="Aplicar",
                on_click=aplicar_dados
            ),

        ]
        self.dialog = ft.AlertDialog(
            title=ft.Text("Digite o nome:"),
            content=dialog_textfield,  # primaria
            actions=material_actions,  # secundaria
        )

        Pagina.PAGE.open(self.dialog)

        Pagina.PAGE.update()

    def alertdialog_banco_inserir(self, nome):

        from front_exe import Pagina

        if nome != "":

            var_contagem = 1
            self.lojadb.inserir_nome_contagem(nome, var_contagem)

            Pagina.PAGE.remove(self.list_view)
            Pagina.PAGE.update()

            self.lj_criar_panellist()
            Pagina.PAGE.update()

            self.snack_bar_floating_button()

        Pagina.PAGE.close(self.dialog)  # Fecha o diálogo
        Pagina.PAGE.update()

    def snack_bar_floating_button(self):

        from front_exe import Pagina

        Pagina.PAGE.open(SnackBar(Text(
            "{} Salvo.".format("tenda"),
            color="#4F4F4F",  # Grey
            size=20,
            weight=FontWeight.W_900
        )))

    #################################################
    #################################################
    def lj_criar_pagina(self):

        from front_exe import Pagina

        self.lj_criar_panellist()
        self.lj_criar_button_lista()
        Pagina.PAGE.update()

    def lj_remover_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.floating_action_button = None

        Pagina.PAGE.remove(self.list_view)

        Pagina.PAGE.update()
