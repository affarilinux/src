from SQLITE.base import BaseSqlite


class SqliteTabela(BaseSqlite):

    def tabela_loja(self) -> None:

        # banco de dados
        self.ativar_with()

        """   teclado       """

        query = """CREATE TABLE if not exists loja(

            ID_loja INTEGER PRIMARY KEY AUTOINCREMENT,

            nome  TEXT,    -- string
            contagem INT   -- estar contando ou nao
            
            )"""
        self.withdb.execute(query)

    def tabela_produto(self):

        # banco de dados
        self.ativar_with()

        """   produto      """

        query = """CREATE TABLE if not exists produto(

            ID_produto INTEGER PRIMARY KEY AUTOINCREMENT,

            nome  TEXT    -- string
            
            )"""
        self.withdb.execute(query)
