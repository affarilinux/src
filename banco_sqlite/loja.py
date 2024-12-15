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
    # seleciona todos nome e contage
    def ljdb_selecionar_nome_contagem(self):

        query = """SELECT nome,contagem FROM loja"""
        self.ativar_with()

        # """SELECT (nome,contagem) FROM loja""" nao funciona assim
        self.withdb.execute(query)
        resultados = self.withdb.fetchall()

        return resultados
    # seleciona uma nome return id

    def ljdb_selecionar_index_nome(self, nome):

        query = """SELECT ID_loja FROM loja WHERE nome = ?"""
        self.ativar_with()

        self.withdb.execute(query, (nome,))
        resultados = self.withdb.fetchall()

        return resultados[0][0]

    def ljdb_selecionar_contagem_valor(self, id):

        query = """SELECT contagem FROM loja WHERE ID_loja = ?"""
        self.ativar_with()

        self.withdb.execute(query, (id,))
        resultados = self.withdb.fetchall()

        return resultados[0][0]

    # seleciona todos nome

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
        self.ativar_banco()

        self.cursorsq.execute(query, (nome, id))

        self.commit_banco()
        self.sair_banco()

    def ljdb_editar_contagem(self, number, id):

        query = """UPDATE loja SET contagem = ? WHERE ID_loja = ?"""

        self.ativar_banco()

        self.cursorsq.execute(query, (number, id))

        self.commit_banco()
        self.sair_banco()

    # remove

    def ljdb_remover_nome_loja(self, nome):

        query = """DELETE FROM loja WHERE nome = ?"""

        self.ativar_banco()

        self.cursorsq.execute(query, (nome, ))

        self.commit_banco()
        self.sair_banco()

    def filtro_frase_nome(self, frase):

        query = """SELECT nome,contagem FROM loja WHERE nome LIKE ?"""
        self.ativar_with()

        self.withdb.execute(query, ('%' + frase + '%',))
        resultados = self.withdb.fetchall()

        return resultados
        # nomes_lojas = [row[0] for row in resultados]

        # return nomes_lojas
