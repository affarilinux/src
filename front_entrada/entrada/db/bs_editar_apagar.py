
from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class dbBSEditar(BaseSqlite):

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
    # select

    def bse_select_query_lista(self, produto):

        querymista = """
        SELECT sp.subnome
        FROM subproduto sp
        INNER JOIN produto p ON sp.id_produto = p.ID_produto
        WHERE p.nome = ?
        """

    # Executa a consulta
        self.withdb.execute(querymista, (produto,))

        # Recupera os subprodutos
        resultados_raw = self.withdb.fetchall()

        # Transforma os resultados no formato AutoCompleteSuggestion

        lista_resultados = [resultado[0] for resultado in resultados_raw]
        # Retorna a lista
        return lista_resultados
