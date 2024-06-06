import os
import time
import keyboard  # "pip install keyboard" no prompt para instalar a biblioteca
import sys

class Banco:
    def __init__(self) -> None:
        pass

    def Saque(self):
        pass

    def Deposito(self):
        pass



class Cliente(Banco):
    def __init__(self, name="", CPF="", nascimento="", email="", celular=""):
        self.usuario = name
        self.CPF = CPF
        self.nascimento = nascimento
        self.email = email
        self.celular = celular
        self.saldo = 0.00

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
                    time.sleep(3)
                    return 0
                else:
                    print("Deposito precisa ser maior que 0")
                    time.sleep(3)
            except:
                print("\nValor invalido! \nretomando operação")
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
                    return 0
                else:
                    print("\nSaldo insuficiente")
                    time.sleep(2)
            except:
                print("\nValor invalido! \nretomando operação")
                time.sleep(3)


    def Perfil(self):
        os.system('cls')
        print("\nPerfil do cliente")
        print(f"Nome: {self.usuario}")
        print(f"CPF: {self.CPF}")
        print(f"Nascimento: {self.nascimento}")
        print(f"Saldo: R$ {self.saldo:.2f}")

        print("\nenter - continuar")
        keyboard.wait("enter")
        sys.stdout.flush()
        print("Retornando ao menu")
        time.sleep(2)



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
                  f"\nenter - Sair")
            opcao = input("--> ")

            if opcao == "": break
            elif opcao == "1": self.cliente.Deposito()
            elif opcao == "2": self.cliente.Saque()
            elif opcao == "3": self.cliente.Perfil()
            else:
                print("Opção invalida")
                time.sleep(4)

    def Login_usuario(self):
        os.system('cls')
        print("Deseja criar um novo usuario ou prosseguir anônimo? \nenter - Criar Usuário \nEsc - Proseguir Anônimo")
        while True:
            key = keyboard.read_key()
            if key == "enter":
                self.Criar_usuario()
                break
            elif key == "esc":
                print("\nIndo para o menu anonimamente \nSeus dados estarão em branco")
                time.sleep(4.5)
                break

    def Criar_usuario(self):
        os.system('cls')
        print("Informações Pessoais")
        self.setings.Alterar_nome()
        self.setings.Alterar_CPF()
        
    def Modificar_usuario(self):
        os.system('cls')
        print("Informe seus dados ou pressione enter para prosseguir")
        input("DEV: 'trabalando nessa parte ainda'")





class Setings:
    def __init__(self, cliente):
        self.cliente = cliente
        self.caractere_especial = "!@#$%&*()_-+={[}]|\:;'<>?,./"
        self.caractere_numero = "0123456789"
        self.caractere_letra = "abcdefghijklmnopqrstuvwxyz"

    def Alterar_nome(self):
        while True:
            os.system('cls')
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
            if any(char in self.caractere_especial for char in cpf) in any(char in self.caractere_numero for char in cpf) or len(cpf)!= 11 or cpf == "":
                print("Seu CPF deve ter 11 numeros e nenhum caractere especial ou letra")
                time.sleep(3)
            else:
                cpf = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]
                self.cliente.CPF = cpf
            break




os.system('cls')
cliente = Cliente()
interface = Interface(cliente)

print("Iniciando Sistema Bancário")
time.sleep(2)


interface.Login_usuario()
interface.Menu()

print("\nSaindo do sistema")
time.sleep(2)
os.system('cls')