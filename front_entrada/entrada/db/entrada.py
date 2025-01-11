
from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class EntradaDB(BaseSqlite):

    def __init__(self):

        pd = SqliteTabela()
        pd.tabela_entrada()

    # insert
    def et_inserir_nome_contagem(self, nome):

        query = """INSERT INTO entrada (nome) VALUES (?)"""
        self.ativar_banco()  # Ativa a conexão

        # Passa a variável nome para o placeholder
        self.cursorsq.execute(query, (nome,))

        self.commit_banco()
        self.sair_banco()

    # select
    # seleciona todos nome e contage
    def et_selecionar_nome(self):

        query = """SELECT nome FROM entrada"""
        self.ativar_with()

        # """SELECT (nome,contagem) FROM loja""" nao funciona assim
        self.withdb.execute(query)
        resultados = self.withdb.fetchall()

        return resultados

    def et_selecionar_index_nome(self, nome):

        query = """SELECT ID_entrada FROM entrada WHERE nome = ?"""
        self.ativar_with()

        self.withdb.execute(query, (nome,))
        resultados = self.withdb.fetchall()

        return resultados[0][0]

    # update

    def et_editar_nome(self, nome, id):

        query = """UPDATE entrada SET nome = ? WHERE ID_entrada = ? """
        self.ativar_banco()

        self.cursorsq.execute(query, (nome, id))

        self.commit_banco()
        self.sair_banco()

    def et_remover_nome(self, nome):

        query = """DELETE FROM entrada WHERE nome = ?"""

        self.ativar_banco()

        self.cursorsq.execute(query, (nome, ))

        self.commit_banco()
        self.sair_banco()

    def et_filtro_frase_nome(self, frase):

        query = """SELECT nome FROM entrada WHERE nome LIKE ?"""
        self.ativar_with()

        self.withdb.execute(query, ('%' + frase + '%',))
        resultados = self.withdb.fetchall()

        return resultados
