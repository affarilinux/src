
from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class DBDialogSPEditar(BaseSqlite):

    def __init__(self):

        subprod = SqliteTabela()
        subprod.tabela_produto()
        subprod.tabela_subproduto()

    """   
        produto    
    """
    # select

    def diaedit_selecionar_index_nome_produto(self, nome):

        query = """SELECT ID_produto FROM produto WHERE nome = ?"""
        self.ativar_with()

        self.withdb.execute(query, (nome,))
        resultados = self.withdb.fetchall()

        return resultados[0][0]

    """
        subproduto
    """
    # select

    def diaedit_selecionar_index_subnome_subproduto(self, nome):

        query = """SELECT ID_subproduto FROM subproduto WHERE subnome = ?"""
        self.ativar_with()

        self.withdb.execute(query, (nome,))
        resultados = self.withdb.fetchall()

        return resultados[0][0]

    # update

    def diaedit_editar_nome(self, novonome, id, sublista):

        query = """UPDATE subproduto SET subnome = ? WHERE 
        id_produto = ? AND ID_subproduto = ?"""
        self.ativar_banco()

        self.cursorsq.execute(query, (novonome, id, sublista))

        self.commit_banco()
        self.sair_banco()

    # deletar

    def diaedit_deletar_nome(self, id, sublista):

        query = """DELETE FROM subproduto 
               WHERE id_produto = ? AND ID_subproduto = ?"""
        self.ativar_banco()

        self.cursorsq.execute(query, (id, sublista))

        self.commit_banco()
        self.sair_banco()
