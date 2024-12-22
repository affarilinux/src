
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
