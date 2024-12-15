from flet import icons, FilledButton, Row, Column

from front_end.loja.LOJA import Loja
from front_end.produto.lista_produto import ListaProduto

from front_end.configuracoes.configuracoes_loja import Configuracoesloja
from front_end.configuracoes.configuracoes_produto import ConfiguracoesProduto


class Configuracoes(
    Configuracoesloja, ConfiguracoesProduto
):

    def __init__(self):

        self.loja_wg = Loja()
        self.lista_prod = ListaProduto()

    def config_criar_button_loja(self):

        def janela_loja(e):

            self.bt_loja()

        # Cria o botão com expand=True
        # lista botoes
        bt_loja = FilledButton(
            " LISTA LOJA",
            icons.ADD_HOME_WORK_ROUNDED,
            expand=True,
            adaptive=True,
            on_click=janela_loja
        )

        self.loja_row = Row(  # Cria o contêiner
            controls=[
                bt_loja
            ],
            expand=True
        )

    def config_criar_button_produtos(self):

        def janela_produto(e):

            self.bt_produto()

        # Cria o botão com expand=True
        # lista botoes
        bt_produto = FilledButton(
            "LISTA PRODUTO",
            icons.SHOPPING_CART_OUTLINED,
            expand=True,
            adaptive=True,
            on_click=janela_produto
        )

        self.produto_row = Row(  # Cria o contêiner
            controls=[
                bt_produto
            ],
            expand=True
        )

    ####################################################
    ####################################################

    def config_criar_pagina(self):
        from front_exe import Pagina
        self.config_criar_button_loja()

        self.config_criar_button_produtos()

        self.lista_wg = Column(
            [
                self.loja_row,
                self.produto_row
            ]
        )
        Pagina.PAGE.add(self.lista_wg)

        Pagina.PAGE.update()

    def config_remover_pagina(self):

        from front_exe import Pagina

        if getattr(self, "lista_wg", None) and self.lista_wg in Pagina.PAGE.controls:
            Pagina.PAGE.controls.remove(self.lista_wg)

        Pagina.PAGE.update()
