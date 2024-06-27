import sqlite3

conn = sqlite3.connect('Banco_de_dados.db')
cursor = conn.cursor()

class Banco_de_dados:
    def __init__(self):
        pass
    
    def Criar_Tabela(self):
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Nome TEXT,
                                CPF TEXT,
                                Idade INTEGER,
                                Senha)''')
        conn.commit

    def criar_usuario_db(self, nome, cpf, idade, senha):
        cursor.execute('''INSERT INTO usuarios(Nome, CPF, Idade, Senha) VALUES(?,?,?,?)''', (nome, cpf, idade, senha))
    
    def fazer_login_db(self, cpf, senha):
        cursor.execute('''SELECT * FROM usuarios WHERE CPF = ? AND Senha = ?''', (cpf, senha))
        if cursor.fetchone():
            print('\nLogin realizado com sucesso')
        else:
            print('\nLogin não realizado')
        input("enter para continuar")


class Interface(Banco_de_dados):
    def __init__(self):
        banco = Banco_de_dados()

    def Menu(self):
        while True:
            print('''
            [1] Cadastrar
            [2] Login
            [3] Sair
            ''')
            opcao = int(input('\nDigite a opção desejada: '))

            if opcao == 1:
                interface.criar_usuario()
            if opcao == 2:
                interface.fazer_login()
            if opcao == 3:
                print('\nSaindo...')
                break

    
    def criar_usuario(self):
        nome = str(input('\nDigite seu nome: '))
        cpf = str(input('Digite seu CPF: '))
        idade = int(input('Digite sua idade: '))
        senha = str(input('Crie sua senha: '))
        self.criar_usuario_db(nome, cpf, idade, senha)

    def fazer_login(self):
        cpf = str(input('Digite seu CPF: '))
        senha = str(input('Digite sua senha: '))
        self.fazer_login_db(cpf, senha)
        



interface = Interface()
banco = Banco_de_dados()
banco.Criar_Tabela()
interface.Menu()
