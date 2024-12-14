from SQLITE.tabela import SqliteTabela
from SQLITE.base import BaseSqlite


class LojaDB(BaseSqlite):

    def __init__(self):

        st = SqliteTabela()
        st.tabela_loja()

    # insert
    def ljdb_inserir_nome_contagem(self, nome, contagem):

        query = """INSERT INTO loja (nome,contagem) VALUES (?,?)"""
        self.ativar_banco()  # Ativa a conexão

        # Passa a variável nome para o placeholder
        self.cursorsq.execute(query, (nome, contagem))

        self.commit_banco()
        self.sair_banco()

    # select
    # seleciona todos
    def ljdb_selecionar_nome_contagem(self):

        query = """SELECT nome,contagem FROM loja"""
        self.ativar_with()

        # """SELECT (nome,contagem) FROM loja""" nao funciona assim
        self.withdb.execute(query)
        resultados = self.withdb.fetchall()

        return resultados
    # seleciona todos

    def ljdb_selecionar_nome(self):

        query = """SELECT nome FROM loja"""
        self.ativar_with()

        # """SELECT (nome,contagem) FROM loja""" nao funciona assim
        self.withdb.execute(query)
        resultados = self.withdb.fetchall()

       # Extrair apenas o nome das lojas
        nomes_lojas = [row[0] for row in resultados]

        return nomes_lojas

    # update

    def ljdb_editar_nome(self, nome, id):

        query = """UPDATE loja SET nome = ? WHERE ID_loja = ? """
        self.ativar_with()

        self.withdb.execute(query, (nome, id))
