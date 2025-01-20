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

    def tabela_subproduto(self):

        # banco de dados
        self.ativar_with()

        """   subproduto      """

        query = """CREATE TABLE if not exists subproduto(

            ID_subproduto INTEGER PRIMARY KEY AUTOINCREMENT,

            id_produto INT,

            subnome  TEXT,    -- string

            FOREIGN KEY (id_produto) REFERENCES produto(ID_produto) 
            ON DELETE CASCADE
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

        self.ativar_with()

        """   subentrada      """

        query = """CREATE TABLE if not exists subentrada(

            ID_subentrada INTEGER PRIMARY KEY AUTOINCREMENT,

            id_entrada INT,

            id_produto   INT,

            id_subproduto  INT,    

            quantidade  INT,

            FOREIGN KEY (id_entrada) REFERENCES entrada(ID_entrada) 
            ON DELETE CASCADE,

            FOREIGN KEY (id_produto) REFERENCES produto(ID_produto) 
            ON DELETE CASCADE,

            FOREIGN KEY (id_subproduto) REFERENCES subproduto(ID_subproduto) 
            ON DELETE CASCADE
            
            )"""

        self.withdb.execute(query)
