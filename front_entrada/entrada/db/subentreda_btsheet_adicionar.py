from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite

from flet import AutoCompleteSuggestion


class SubEntradaBtsheetAdicionarDB(SqliteTabela, BaseSqlite):

    def __init__(self):
        super().__init__()

        sub_btshhet = SqliteTabela()

        sub_btshhet.tabela_entrada()
        sub_btshhet.tabela_subentrada()
        sub_btshhet.tabela_produto()
        sub_btshhet.tabela_subproduto()

    """
        PRODUTO
    """
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

    """
         QUERY MISTA
    """
    # select

    def sheadic_select_listaquery_subentrada(self, produto):

        # Define a consulta para buscar subprodutos pelo nome do produto
        query = """
        SELECT sp.subnome
        FROM subproduto sp
        INNER JOIN produto p ON sp.id_produto = p.ID_produto
        WHERE p.nome = ?
        """

        self.ativar_with()
        # Executa a consulta
        self.withdb.execute(query, (produto,))

        # Recupera os subprodutos
        resultados_raw = self.withdb.fetchall()

        # Transforma os resultados no formato AutoCompleteSuggestion

        lista_resultados = [resultado[0] for resultado in resultados_raw]
        # Retorna a lista
        return lista_resultados

    def sheadic_select_query_tripla(self, entrada):

        self.ativar_with()

        querymista = """
        SELECT
            p.nome, sp.subnome, se.quantidade
        FROM
            subentrada se
        INNER JOIN
            entrada et ON se.id_entrada = et.ID_entrada
        INNER JOIN
            produto p ON se.id_produto = p.ID_produto
        LEFT JOIN
            subproduto sp ON se.id_subproduto = sp.ID_subproduto
        WHERE
            et.nome = ?
        """

        self.withdb.execute(querymista, (entrada,))
        # Recupera os subprodutos
        resultados_raw = self.withdb.fetchall()

        # lista_resultados = [(row[0], row[1], row[2]) for row in resultados_raw]
        lista_resultados = [
            (row[0], row[1] if row[1] is not None else "*S/subproduto", row[2])
            for row in resultados_raw
        ]

        return lista_resultados

    def sheadic_select_query_dupla__len_subp(self, entrada, produto,
                                             subproduto):

        self.ativar_with()

        querymista = """
        SELECT
            p.nome, sp.subnome
        FROM
            subentrada se
        INNER JOIN
            entrada et ON se.id_entrada = et.ID_entrada
        INNER JOIN
            produto p ON se.id_produto = p.ID_produto
        LEFT JOIN
            subproduto sp ON se.id_subproduto = sp.ID_subproduto
        WHERE
            et.nome = ? AND p.nome = ? AND sp.subnome = ?
        """

        self.withdb.execute(
            querymista, (entrada, produto, subproduto))

        resultados_raw = self.withdb.fetchall()

        """lista_resultados = [
            (row[0], row[1] if row[1] is not None else "*S/subproduto")
            for row in resultados_raw
        ]"""
        lista_resultados = [(row[0], row[1]) for row in resultados_raw]
        return lista_resultados

    def sheadic_select_query_dupla__len_s_subp(self, entrada, produto):

        self.ativar_with()

        querymista = """
        SELECT
            p.nome
        FROM
            subentrada se
        INNER JOIN
            entrada et ON se.id_entrada = et.ID_entrada
        INNER JOIN
            produto p ON se.id_produto = p.ID_produto
        LEFT JOIN
            subproduto sp ON se.id_subproduto = sp.ID_subproduto
        WHERE
            et.nome = ? AND p.nome = ?
        """

        self.withdb.execute(
            querymista, (entrada, produto))

        resultados_raw = self.withdb.fetchall()

        """lista_resultados = [
            (row[0], row[1] if row[1] is not None else "*S/subproduto")
            for row in resultados_raw
        ]"""
        lista_resultados = [(row[0]) for row in resultados_raw]
        return lista_resultados
    # insert

    def sheadic_insert_query_tripla(
            self, entrada, produto, subproduto, quantidade):

        self.ativar_banco()  # Ativa a conexão

        querymista = """INSERT INTO subentrada (
        id_entrada, id_produto, id_subproduto, quantidade)
        VALUES (
        (SELECT ID_entrada FROM entrada WHERE nome = ?),
        (SELECT ID_produto FROM produto WHERE nome = ?),
        (SELECT ID_subproduto FROM subproduto WHERE subnome = ?),
        ?
        )"""

        self.cursorsq.execute(
            querymista, (entrada, produto, subproduto, quantidade))

        self.commit_banco()
        self.sair_banco()
