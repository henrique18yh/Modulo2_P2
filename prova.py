import sqlite3
1-'CRIAR O BANCO'
# Conexão com o banco
conn = sqlite3.connect("Escola.db")
cursor = conn.cursor()


2-'CRIAR TABELA'
cursor.execute("""
CREATE TABLE IF NOT EXISTS Alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT
    
)
""")
3-'INSERIR REGISTROS NA TABELA'
#cursor.execute("INSERT INTO Alunos (nome,idade,email) VALUES (?,?,?)", ('joao','19','joao@gmail.com'))
#cursor.execute("INSERT INTO Alunos (nome,idade,email) VALUES (?,?,?)" , ('Ricardo','19','Ricardomelhor@gmail.com)'))
#cursor.execute("INSERT INTO Alunos (nome,idade,email) VALUES (?,?,?)" , ('PauloValero','14','Paulo@gmail.com'))


4-'LISTAR TODOS NA TABELA'#cursor.execute("SELECT * FROM Alunos ")


5-'BUSCAR ALUNOS POR ID'#cursor.execute ("SELECT nome FROM Alunos WHERE id = 2")
6-'ATUALIZAR REGISTROS'#cursor.execute ("UPDATE Alunos SET nome = 'Victor' WHERE nome = 'PauloValero' ")
7-'DELETAR REGISTROS'#cursor.execute ("DELETE FROM Alunos WHERE id = 2")
print(cursor.fetchall())

conn.commit()


