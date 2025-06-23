import sqlite3

# Função para conectar ao banco
def conectar():
    conexao = sqlite3.connect('sqlite/labagenda.db')
    return conexao

# Função para criar a tabela (executa no início)
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            descricao TEXT
        )
    ''')

    conexao.commit()
    conexao.close()
