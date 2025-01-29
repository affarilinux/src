

class Menores:

    def lista_entrada_sqlite(self):  # multiplas funcoes

        varlist_produto = self.et_selecionar_nome()  # Obtém os dados da tabela

        return varlist_produto[:: -1]

    def text_filtro_entrada(self, frase):

        from front_exe import Pagina

        Pagina.PAGE.remove(self.list_view_ent)
        Pagina.PAGE.update()

        filtro = self.et_filtro_frase_nome(frase)
        self.pd_criar_panellist(filtro[:: -1])
        Pagina.PAGE.update()

    def remover_nome_entrada(self, titulo):

        from front_exe import Pagina

        var_existe = self.et_select_existe_subentrada(titulo)

        if len(var_existe) == 0:

            self.et_remover_nome(titulo)

            Pagina.PAGE.remove(self.list_view_ent)
            Pagina.PAGE.update()

            self.pd_criar_panellist(
                self.lista_entrada_sqlite()
            )
            Pagina.PAGE.update()

        elif len(var_existe) > 0:

            from front_end.menor import Menor

            class_menor = Menor()

            class_menor.snack_bar_floating_button(
                "Possui itens na lista {}.".format(titulo))
