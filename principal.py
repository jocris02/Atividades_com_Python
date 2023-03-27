import sqlite3 as conector

conexao = None
cursor = None

try:
    conexao = conector.connect("meu_banco2.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    comando = '''CREATE TABLE Municipio(
                    codigo INTEGER NOT NULL,
                    nome VARCHAR(32) NOT NULL,
                    PRIMARY KEY (codigo)
                    );'''
    cursor.execute(comando)

    comando = '''CREATE TABLE Populacao(
                    codigo INTEGER NOT NULL,
                    ano INTEGER NOT NULL,
                    PRIMARY KEY (codigo, ano),
                    FOREIGN KEY(codigo) REFERENCES Municipio(codigo)
                    );'''
    cursor.execute(comando)

    comando = '''CREATE TABLE Dengue(
                    codigo INTEGER NOT NULL,
                    ano INTEGER NOT NULL,
                    casos INTEGER NOT NULL,
                    PRIMARY KEY (codigo, ano),
                    FOREIGN KEY(codigo) REFERENCES Municipio(codigo)
                    );'''
    cursor.execute(comando)

    conexao.commit()
except conector.DatabaseError as erro:
    cursor = conexao.cursor()
    print(f"Erro de banco de dados: {erro}")

finally:
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()
