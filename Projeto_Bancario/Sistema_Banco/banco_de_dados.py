import sqlite3

conexao = sqlite3.connect('Banco.db')
cursor = conexao.cursor()


cursor.execute( '''  
    CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf TEXT,
    ddd TEXT,
    numero TEXT,
    email TEXT,
    data TEXT,
    CEP TEXT,
    rua TEXT,
    Ncasa TEXT,
    senha TEXT,
    saldo INTEGER)
                ''' )


def Cadastro_db(nome, cpf, ddd, numero, email, data, CEP, rua, Ncasa, senha):
    cursor.execute("INSERT INTO cliente (nome, cpf, ddd, numero, email, data, CEP, rua, Ncasa, senha, saldo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (nome, cpf, ddd, numero, email, data, CEP, rua, Ncasa, senha, 0))
    conexao.commit()
    print('Cadastro realizado com sucesso!')


def Login_db(cpf, senha):
    if not cpf or not senha:
        return False
    
    cursor.execute("SELECT * FROM cliente WHERE cpf =? AND senha =?", (cpf, senha))
    result = cursor.fetchall()
    if result:
        return True
    else:
        return False
    

def Informacoes_db(cpf):
    cursor.execute("SELECT * FROM cliente WHERE cpf =?" (cpf))
    result = cursor.fetchall()
    if result:
        return result[0][10]
    else:
        return False
    

def Saque(cpf, saldo):
    cursor.execute("UPDATE cliente SET saldo = ? WHERE cpf = ?" (saldo, cpf))


def Deposito(cpf, saldo):
    cursor.execute("UPDATE cliente SET saldo = ? WHERE cpf = ?" (saldo, cpf))


def Fechar_db():
    conexao.close()
