

class Menores:

    def lista_loja_sqlite(self):

        # Supondo que varlist_loja é uma lista de tuplas [(loja_nome, status), ...]
        varlist_loja = self.ljdb_selecionar_nome_contagem()  # Obtém os dados da tabela

        return varlist_loja

    def text_filtro(self, frase):

        from front_exe import Pagina

        Pagina.PAGE.remove(self.list_view)
        Pagina.PAGE.update()

        self.lj_criar_panellist(
            self.filtro_frase_nome(frase)
        )
        Pagina.PAGE.update()

    def remover_nome_loja(self, titulo):

        from front_exe import Pagina

        self.ljdb_remover_nome_loja(titulo)

        Pagina.PAGE.remove(self.list_view)
        Pagina.PAGE.update()

        self.lj_criar_panellist(
            self.lista_loja_sqlite()
        )
        Pagina.PAGE.update()

    def mudar_status_loja(self, titulo):

        index = self.ljdb_selecionar_index_nome(titulo)

        conta = self.ljdb_selecionar_contagem_valor(index)

        if conta == 1:

            self.ljdb_editar_contagem(0, index)

        elif conta == 0:

            self.ljdb_editar_contagem(1, index)
