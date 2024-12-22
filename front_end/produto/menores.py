class Menores:

    def lista_produto_sqlite_produto(self):  # multiplas funcoes

        varlist_produto = self.pddb_selecionar_nome()  # Obtém os dados da tabela

        return varlist_produto

    def text_filtro_produto(self, frase):

        from front_exe import Pagina

        Pagina.PAGE.remove(self.list_view_pd)
        Pagina.PAGE.update()

        self.pd_criar_panellist(
            self.filtro_frase_nome_produto(frase)
        )
        Pagina.PAGE.update()

    def remover_nome_produto(self, titulo):

        from front_exe import Pagina

        self.pddb_remover_nome_loja(titulo)

        Pagina.PAGE.remove(self.list_view_pd)
        Pagina.PAGE.update()

        self.pd_criar_panellist(
            self.lista_produto_sqlite_produto()
        )
        Pagina.PAGE.update()
