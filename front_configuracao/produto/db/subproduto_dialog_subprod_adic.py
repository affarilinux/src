from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class SubprodutoDialogSubprodutoAdicionar(BaseSqlite):

    def __init__(self):

        subprod = SqliteTabela()
        subprod.tabela_produto()
        subprod.tabela_subproduto()

    """   
        produto    
    """
    # select

    def subpro_selecionar_index_nome_produto(self, nome):

        query = """SELECT ID_produto FROM produto WHERE nome = ?"""
        self.ativar_with()

        self.withdb.execute(query, (nome,))
        resultados = self.withdb.fetchall()

        return resultados[0][0]

    """
        subproduto
    """

    # insert

    def subpro_inserir_nome_subproduto(self, index_produto, nome):

        query = """
        INSERT INTO subproduto (id_produto,subnome) VALUES (?,?)"""
        self.ativar_banco()  # Ativa a conexão

        self.cursorsq.execute(query, (index_produto, nome))

        self.commit_banco()
        self.sair_banco()

    """
        query mista
    """

    def subpro_queryrepetido(self, nome_produto, subnome):

        self.ativar_with()

        # Query SQL para verificar duplicidade
        query = """
        WITH produto_id AS (
            SELECT ID_produto
            FROM produto
            WHERE nome = ?
        )
        SELECT COUNT(*) AS qtd_repetidos
        FROM subproduto
        WHERE id_produto = (SELECT ID_produto FROM produto_id)
        AND subnome = ?;
        """

        # Executa a query com os parâmetros
        cursor = self.withdb.execute(query, (nome_produto, subnome))
        result = cursor.fetchone()

        # Retorna True se duplicado, False caso contrário
        return result[0] > 0
