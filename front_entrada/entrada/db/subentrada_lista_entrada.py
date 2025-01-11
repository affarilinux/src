
from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class SubEntradaDB(BaseSqlite):

    def __init__(self):
        super().__init__()

        sub_enter = SqliteTabela()
        sub_enter.tabela_subentrada()

    # select
    def subent_query_lista(self, id_entrada):

        # Ativa a conexão com o banco de dados
        self.ativar_with()

        # Query para encontrar subentradas pelo ID_entrada
        query = """
                SELECT 
                entrada.nome AS nome_entrada,
                subentrada.sub_nome,
                subentrada.quantidade
                FROM 
                    subentrada
                JOIN 
                    entrada
                ON 
                    subentrada.id_nome = entrada.ID_entrada
                WHERE 
                subentrada.id_nome = ?;

            """

        # Executa a consulta com o parâmetro
        self.withdb.execute(query, (id_entrada,))
        resultados = self.withdb.fetchall()

        # Retorna os resultados
        return resultados
