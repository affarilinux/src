from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite

from flet import AutoCompleteSuggestion


class SubEntradaBtsheetAdicionarDB(SqliteTabela, BaseSqlite):

    def __init__(self):
        super().__init__()

        sub_btshhet = SqliteTabela()
        sub_btshhet.tabela_subentrada()
        sub_btshhet.tabela_subproduto()

    # select
    def sheadic_select_lista_entrada(self):

        self.ativar_with()

        query = """SELECT nome FROM produto"""
        self.ativar_with()

        # """SELECT (nome,contagem) FROM loja""" nao funciona assim
        self.withdb.execute(query)
        # Recupera todos os resultados
        resultados_raw = self.withdb.fetchall()

        # Transforma os resultados no formato AutoCompleteSuggestion
        produto_sugestoes = [
            AutoCompleteSuggestion(key=resultado[0], value=resultado[0])
            for i, resultado in enumerate(resultados_raw)
        ]

        # Retorna a lista
        return produto_sugestoes

    def sheadic_select_listaquery_subentrada(self, produto):

        self.ativar_with()

        self.ativar_with()

        # Define a consulta para buscar subprodutos pelo nome do produto
        query = """
        SELECT sp.subnome
        FROM subproduto sp
        INNER JOIN produto p ON sp.id_produto = p.ID_produto
        WHERE p.nome = ?
        """

        # Executa a consulta
        self.withdb.execute(query, (produto,))

        # Recupera os subprodutos
        resultados_raw = self.withdb.fetchall()

        # Transforma os resultados no formato AutoCompleteSuggestion
        """produto_sugestoes = [
            AutoCompleteSuggestion(key=resultado[0], value=resultado[0])
            for i, resultado in enumerate(resultados_raw)
        ]"""

        lista_resultados = [resultado[0] for resultado in resultados_raw]
        # Retorna a lista
        return lista_resultados
