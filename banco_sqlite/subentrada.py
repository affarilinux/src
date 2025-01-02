
from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class SubEntradaDB(BaseSqlite):

    def __init__(self):

        sub_ent = SqliteTabela()
        sub_ent.tabela_subentrada()
