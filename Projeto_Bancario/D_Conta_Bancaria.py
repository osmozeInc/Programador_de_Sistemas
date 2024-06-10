import os
import time
import keyboard  # type: ignore # "pip install keyboard" no prompt para instalar a biblioteca
import sys
import re
from datetime import datetime



class Cliente:
    def __init__(self, name="", CPF="", nascimento="", email="", celular="", senha=""):
        self.usuario = name
        self.CPF = CPF
        self.nascimento = nascimento
        self.email = email
        self.celular = celular
        self.senha = senha
        self.saldo = 0.00
        self.interface = Interface(self)

    def Deposito(self):
        print("\nComeçando operação de deposito")
        time.sleep(3)

        while True:
            os.system('cls')
            try:
                deposito = input(f"Saldo: R$ {self.saldo:.2f} \nQuanto quer depositar? \n--> ")
                deposito = float(deposito)
                if deposito > 0:
                    self.saldo += deposito
                    print(f"\nDeposito de R$ {deposito:.2f} realizado com sucesso!")
                    break
                elif deposito == 0:
                    print("\nDeposito cancelado")
                    break
                else:
                    print("Deposito precisa ser maior que 0")
                    time.sleep(3)
            except:
                print("\nValor invalido! \nretomando operação")
                time.sleep(3)
        time.sleep(3)

    def Saque(self):
        print("\nComeçando operação de Saque")
        time.sleep(3)

        while True:
            os.system('cls')

            try:
                saque = input(f"Saldo: R$ {self.saldo:.2f} \nQuanto quer sacar: \n--> ")
                saque = float(saque)
                if saque > 0 and saque <= self.saldo:
                    self.saldo -= saque
                    print(f"\nSaque de R$ {saque:.2f} realizado com sucesso!")
                    break
                if saque == 0:
                    print("\nSaque cancelado")
                    time.sleep(3)
                    break
                else:
                    print("\nSaldo insuficiente")
                    time.sleep(2)
            except:
                print("\nValor invalido! \nretomando operação")
                time.sleep(3)
        time.sleep(3)

    def Perfil(self):
        os.system('cls')
        print(f"\nPerfil do cliente"
              f"\nNome: {self.usuario}"
              f"\nCPF: {self.CPF}"
              f"\nNascimento: {self.nascimento}"
              f"\nEmail: {self.email}"
              f"\nCelular: {self.celular}")

        print("\nEnter - Menu \nEsc - Editar informações")
        while True:
            key = keyboard.read_event()
            if key.event_type == 'down':
                if key.name == "enter":
                    break
                if key.name == "esc":
                    self.interface.Criar_usuario()
                    break   




class Interface:
    def __init__(self, cliente):
        self.cliente = cliente
        self.setings = Setings(cliente)

    def Menu(self):
        while True:
            sys.stdout.flush()
            os.system('cls')
            print("Bem vindo, " + self.cliente.usuario)
            print(f"\nSelecione uma opção"
                  f"\n----------------------"
                  f"\n1 - Realizar deposito"
                  f"\n2 - Realizar saque"
                  f"\n3 - Ver perfil"
                  f"\nenter - Sair"
                  f"\n--> ", end='')
            opcao = input()

            if opcao == "": break
            elif opcao == "1": self.cliente.Deposito()
            elif opcao == "3": self.cliente.Perfil()
            elif opcao == "2": self.cliente.Saque()
            else:
                print("Opção invalida")
                time.sleep(3)

    def Login_usuario(self):
        os.system('cls')
        print("Deseja criar um novo usuario ou prosseguir anônimo? \nenter - Criar Usuário \nEsc - Proseguir Anônimo")
        while True:
            key = keyboard.read_event()
            if key.name == "enter":
                input()
                self.Criar_usuario()
                break
            elif key.name == "esc":
                print("\nIndo para o menu anonimamente \nSeus dados estarão em branco")
                time.sleep(4)
                break

    def Criar_usuario(self):
        self.setings.Alterar_nome()
        self.setings.Alterar_CPF()
        self.setings.Alterar_nascimento()
        self.setings.Alterar_email()
        self.setings.Alterar_celular()
        self.setings.Alterar_senha()



class Setings:
    def __init__(self, cliente):
        self.cliente = cliente
        self.caractere_especial = "!@#$%&*()_-+={[}]|\:;'<>?,./"
        self.caractere_numero = "0123456789"
        self.caractere_letra = "abcdefghijklmnopqrstuvwxyz"
        self.email_padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    def Alterar_nome(self):
        while True:
            os.system('cls')
            sys.stdout.flush()
            name = input("Nome: ")
            if any(char in self.caractere_especial for char in name) or any(char in self.caractere_numero for char in name) or name == "":
                print("Nome não pode conter caracteres especiais ou numeros")
                time.sleep(3)
            else:
                name = name.lower().title().strip()
                self.cliente.usuario = name
                break

    def Alterar_CPF(self):
        while True:
            os.system('cls')
            cpf = input("CPF: ")
            if any(char in self.caractere_especial for char in cpf) or any(char in self.caractere_letra for char in cpf) or len(cpf)!= 11:
                print("Seu CPF deve ter 11 numeros e nenhum caractere especial ou letra")
                time.sleep(3)
            else:
                self.cliente.CPF = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]
                break

    def Alterar_nascimento(self):
        while True:
            os.system('cls')
            nascimento = input("Data de nascimento \nDia: ")
            nascimento += input("Mês: ")
            nascimento += input("Ano: ")
            if any(char in self.caractere_especial for char in nascimento) or any(char in self.caractere_letra for char in nascimento) or len(nascimento)!= 8:
                print("A data especificada é inválida")
                time.sleep(3)
            else:
                nascimento = nascimento[:2] + "/" + nascimento[2:4] + "/" + nascimento[4:]
                try:
                    data = datetime.strptime(nascimento, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Data invalida!")
                    time.sleep(3)
        self.cliente.nascimento = nascimento

    def Alterar_email(self):
        while True:
            os.system('cls')
            email = input("Email: ")
            if not re.match(self.email_padrao, email):
                print("Email inválido!")
                time.sleep(3)
            else:
                self.cliente.email = email
                break

    def Alterar_celular(self):
        while True:
            os.system('cls')
            celular = input("Numero do celular \n+55 DDD: ")
            if any(char in self.caractere_especial for char in celular) or any(char in self.caractere_letra for char in celular) or len(celular)!= 2:
                print("DDD invalido!")
                time.sleep(3)
            else:
                while True:
                    os.system('cls')
                    celular += input(f"Numero do celular \n+55 ({celular}) 9")
                    if any(char in self.caractere_especial for char in celular) or any(char in self.caractere_letra for char in celular) or len(celular)!= 10:
                        print("Seu celular deve ter 8 numeros e nenhum caractere especial")
                        time.sleep(3)
                    else:
                        self.cliente.celular = celular
                        break
                break

    def Alterar_senha(self):
        while True:
            os.system('cls')
            
            print("Digite sua senha: ")
            senha_1 = self.Seguranca_senha()
            print("Confirme sua senha: ")
            senha_2 = self.Seguranca_senha()
            if senha_1 != senha_2:
                print("As senhas não coincidem!")
                time.sleep(3)
            else:
                self.cliente.senha = senha_1
                break
        input()
        input()
        sys.stdout.flush()

    def Seguranca_senha(self):
        senha = ''
        while True:
            tecla = keyboard.read_event()
            if tecla.event_type == 'down':
                if tecla.name == 'enter':
                    break
                elif tecla.name == 'backspace':
                    senha += senha[:-1]
                    print("\b \b", end="", flush=True)
                else:
                    senha += tecla.name
                    print("*", end="", flush=True)
        print()
        return senha




os.system('cls')
cliente = Cliente()
interface = Interface(cliente)
settings = Setings(cliente)

print("Iniciando Sistema Bancário")
time.sleep(2)

interface.Login_usuario()
interface.Menu()

print("\nSaindo do sistema")
time.sleep(2)
os.system('cls')


# DEV: MELHORIAS PARA PESQUISAR: 
#
# colocar mais critérios para o email ser aceito
# colocar mais critérios para a senha ser aceita
# adicionar seção para editar os dados
# adicionar o extrato