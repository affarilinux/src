
from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class dbDialogeditApagar(BaseSqlite):

    def __init__(self):
        super().__init__()

        sub_btshhet = SqliteTabela()

        sub_btshhet.tabela_entrada()
        sub_btshhet.tabela_subentrada()
        sub_btshhet.tabela_produto()
        sub_btshhet.tabela_subproduto()
    """
        query mista
    """
    # update

    def dbdea_update_mumero_subentrada_trilo(self, entrada, produto,
                                             subproduto, numero):

        querymista = """
        UPDATE subentrada
        SET quantidade = ?
        WHERE 
            id_entrada = (SELECT ID_entrada FROM entrada WHERE nome = ?)
            AND id_produto = (SELECT ID_produto FROM produto WHERE nome = ?)
            AND id_subproduto = (SELECT ID_subproduto FROM subproduto WHERE subnome = ?)
        """
        self.ativar_banco()

        self.cursorsq.execute(querymista, (numero, entrada, produto,
                                           subproduto))

        self.commit_banco()
        self.sair_banco()

    def dbdea_update_mumero_subentrada_dupla(self, entrada, produto,
                                             numero):

        querymista = """
        UPDATE subentrada
        SET quantidade = ?
        WHERE 
            id_entrada = (SELECT ID_entrada FROM entrada WHERE nome = ?)
            AND id_produto = (SELECT ID_produto FROM produto WHERE nome = ?)
           
        """
        self.ativar_banco()

        self.cursorsq.execute(querymista, (numero, entrada, produto))

        self.commit_banco()
        self.sair_banco()

    # delete

    def dbdea_delete_subentrada_trilo(self, entrada, produto,
                                      subproduto):

        query = """
        DELETE FROM subentrada 
        WHERE 
            id_entrada = (SELECT ID_entrada FROM entrada WHERE nome = ?)
            AND id_produto = (SELECT ID_produto FROM produto WHERE nome = ?)
            AND id_subproduto = (SELECT ID_subproduto FROM subproduto WHERE subnome = ?)"""

        self.ativar_banco()

        self.cursorsq.execute(query, (entrada, produto, subproduto))

        self.commit_banco()
        self.sair_banco()

    def dbdea_delete_subentrada_duplo(self, entrada, produto):

        query = """
        DELETE FROM subentrada 
        WHERE 
            id_entrada = (SELECT ID_entrada FROM entrada WHERE nome = ?)
            AND id_produto = (SELECT ID_produto FROM produto WHERE nome = ?) """

        self.ativar_banco()

        self.cursorsq.execute(query, (entrada, produto))

        self.commit_banco()
        self.sair_banco()
