import sqlite3

conexao = sqlite3.connect('Supermercado.db')
cursor = conexao.cursor()


cursor.execute( '''  
    CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf TEXT,
    ddd TEXT,
    numero TEXT,
    email TEXT,
    departamento TEXT,
    cargo TEXT,
    senha TEXT)
                ''' )


def Cadastro_db(nome, cpf, ddd, numero, email, departamento, cargo, senha):
    cursor.execute("INSERT INTO funcionarios (nome, cpf, ddd, numero, email, departamento, cargo, senha) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nome, cpf, ddd, numero, email, departamento, cargo, senha))
    conexao.commit()
    print('Cadastro realizado com sucesso!')


def Login_db(cpf, senha, departamento):
    cursor.execute("SELECT * FROM funcionarios WHERE cpf =? AND senha =? AND departamento =?", (cpf, senha, departamento))
    result = cursor.fetchall()
    if result:
        return True
    else:
        return False
    
def Fechar_db():
    conexao.close()