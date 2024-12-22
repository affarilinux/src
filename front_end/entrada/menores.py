from flet import Text, IconButton, icons


class Menores:

    def lista_entrada_sqlite(self):  # multiplas funcoes

        varlist_produto = self.et_selecionar_nome()  # Obtém os dados da tabela

        return varlist_produto[:: -1]

    def text_filtro_entrada(self, frase):

        from front_exe import Pagina

        Pagina.PAGE.remove(self.list_view_ent)
        Pagina.PAGE.update()

        self.pd_criar_panellist(
            self.filtro_frase_nome_produto(frase)
        )
        Pagina.PAGE.update()

    def remover_nome_entrada(self, titulo):

        from front_exe import Pagina

        self.pddb_remover_nome_loja(titulo)

        Pagina.PAGE.remove(self.list_view_ent)
        Pagina.PAGE.update()

        self.pd_criar_panellist(
            self.lista_entrada_sqlite()
        )
        Pagina.PAGE.update()
