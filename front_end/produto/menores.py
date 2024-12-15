class Menores:

    def remover_nome_produto(self, titulo):

        from front_exe import Pagina

        self.pddb_remover_nome_loja(titulo)

        Pagina.PAGE.remove(self.list_view_pd)
        Pagina.PAGE.update()

        self.pd_criar_panellist()
        Pagina.PAGE.update()
