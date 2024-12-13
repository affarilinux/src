import sqlite3


class BaseSqlite:

    def ativar_with(self):

        with sqlite3.connect('SQLITE/IA.db') as conn:

            self.withdb = conn.cursor()

    def ativar_banco(self):

        self.bancovar = sqlite3.connect('SQLITE/IA.db')
        self.cursorsq = self.bancovar.cursor()

    def commit_banco(self):

        self.bancovar.commit()

    def sair_banco(self):

        self.cursorsq.close()
        self.bancovar.close()