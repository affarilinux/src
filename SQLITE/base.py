import sqlite3


class BaseSqlite:

    def ativar_with(self):

        # nao funciona com commit()
        with sqlite3.connect('SQLITE/estoque.db') as conn:

            self.withdb = conn.cursor()

    def ativar_banco(self):

        self.bancovar = sqlite3.connect('SQLITE/estoque.db')
        self.cursorsq = self.bancovar.cursor()

    def commit_banco(self):

        self.bancovar.commit()

    def sair_banco(self):

        self.cursorsq.close()
        self.bancovar.close()
