from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class ProdutoDB(BaseSqlite):

    def __init__(self):

        pd = SqliteTabela()
        pd.tabela_produto()

    # select
    # seleciona todos nome e contage
    def ljdb_selecionar_nome(self):

        query = """SELECT nome FROM produto"""
        self.ativar_with()

        # """SELECT (nome,contagem) FROM loja""" nao funciona assim
        self.withdb.execute(query)
        resultados = self.withdb.fetchall()

        return resultados
