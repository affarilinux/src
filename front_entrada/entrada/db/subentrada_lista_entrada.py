
from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class SubEntradaDB(BaseSqlite):

    def __init__(self):
        super().__init__()

        print(234)
        sub_enter = SqliteTabela()
        sub_enter.tabela_subentrada()

    # select
    def subent_query_lista(self, id_entrada):
        """
        Lista todas as subentradas relacionadas a um ID_entrada específico.

        Args:
            id_entrada (int): O ID da entrada para buscar as subentradas.

        Returns:
            list: Lista de subentradas associadas ao ID_entrada.
        """
        try:
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

        except Exception as e:
            print(f"Erro ao buscar subentradas para ID_entrada {
                  id_entrada}: {e}")
            return []
