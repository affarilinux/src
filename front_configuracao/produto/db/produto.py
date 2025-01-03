from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class ProdutoDB(BaseSqlite):

    def __init__(self):

        pd = SqliteTabela()
        pd.tabela_produto()

    # insert
    def pddb_inserir_nome_contagem(self, nome):

        query = """INSERT INTO produto (nome) VALUES (?)"""
        self.ativar_banco()  # Ativa a conexão

        # Passa a variável nome para o placeholder
        self.cursorsq.execute(query, (nome,))

        self.commit_banco()
        self.sair_banco()

    # select
    # seleciona todos nome e contage
    def pddb_selecionar_nome(self):

        query = """SELECT nome FROM produto"""
        self.ativar_with()

        # """SELECT (nome,contagem) FROM loja""" nao funciona assim
        self.withdb.execute(query)
        resultados = self.withdb.fetchall()

        return resultados

    def pddb_selecionar_index_nome(self, nome):

        query = """SELECT ID_produto FROM produto WHERE nome = ?"""
        self.ativar_with()

        self.withdb.execute(query, (nome,))
        resultados = self.withdb.fetchall()

        return resultados[0][0]

    # update

    def pddb_editar_nome(self, nome, id):

        query = """UPDATE produto SET nome = ? WHERE ID_produto = ? """
        self.ativar_banco()

        self.cursorsq.execute(query, (nome, id))

        self.commit_banco()
        self.sair_banco()

    # remove

    def pddb_remover_nome_loja(self, nome):

        query = """DELETE FROM produto WHERE nome = ?"""

        self.ativar_banco()

        self.cursorsq.execute(query, (nome, ))

        self.commit_banco()
        self.sair_banco()

    # filtro
    def filtro_frase_nome_produto(self, frase):

        query = """SELECT nome FROM produto WHERE nome LIKE ?"""
        self.ativar_with()

        self.withdb.execute(query, ('%' + frase + '%',))
        resultados = self.withdb.fetchall()

        return resultados
