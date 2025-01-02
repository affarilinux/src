from SQLITE.base import BaseSqlite


class SqliteTabela(BaseSqlite):

    def tabela_loja(self) -> None:

        # banco de dados
        self.ativar_with()

        """   Loja      """

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

    def tabela_entrada(self):

        # banco de dados
        self.ativar_with()

        """   entrada      """

        query = """CREATE TABLE if not exists entrada(

            ID_entrada INTEGER PRIMARY KEY AUTOINCREMENT,

            nome  TEXT    -- string

            )"""

        self.withdb.execute(query)

    def tabela_subentrada(self):

        # banco de dados
        self.ativar_with()

        """   subentrada      """

        query = """CREATE TABLE if not exists subentrada(

            ID_subentrada INTEGER PRIMARY KEY AUTOINCREMENT,

            id_nome   INT,

            sub_nome  TEXT,    -- string

            quantidade  INT,

            FOREIGN KEY (id_nome) REFERENCES entrada(ID_entrada) 
            ON DELETE CASCADE
            
            )"""

        self.withdb.execute(query)
