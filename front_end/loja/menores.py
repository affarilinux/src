

class Menores:

    def remover_nome_loja(self, titulo):

        from front_exe import Pagina

        self.ljdb_remover_nome_loja(titulo)

        Pagina.PAGE.remove(self.list_view)
        Pagina.PAGE.update()

        self.lj_criar_panellist()
        Pagina.PAGE.update()

    def mudar_status_loja(self, titulo):

        index = self.ljdb_selecionar_index_nome(titulo)

        conta = self.ljdb_selecionar_contagem_valor(index)

        if conta == 1:

            self.ljdb_editar_contagem(0, index)

        elif conta == 0:

            self.ljdb_editar_contagem(1, index)
