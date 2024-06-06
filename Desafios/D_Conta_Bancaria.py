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
    def __init__(self, name = "", CPF = "", nascimento = ""):
        self.usuario = name
        self.CPF = CPF
        self.nascimento = nascimento
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

        return print(f"\nDeposito de R$ {deposito:.2f} realizado com sucesso!")

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

        return print(f"\nSaque de R$ {saque:.2f} realizado com sucesso!")

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



class Interface():
    def Menu(self):
        while True:
            sys.stdout.flush()
            os.system('cls')
            print("Bem vindo, " + cliente.usuario)
            print(f"\nSelecione uma opção"
                f"\n----------------------"
                f"\n1 - Realizar deposito"
                f"\n2 - Realizar saque"
                f"\n3 - Ver perfil"
                f"\nenter - Sair")
            opcao = input("--> ")
            
            if opcao == "": break
            elif opcao == "1": cliente.Deposito()
            elif opcao == "2": cliente.Saque()
            elif opcao == "3": cliente.Perfil()
            else:
                print("Opção invalida")
                time.sleep(4)

    def Criar_usuario(self):
        os.system('cls')
        print("Deseja criar um novo usuario ou prosseguir anônimo? \nenter - Sim \nEsc - Não")
        while True:
            key = keyboard.read_key()
            if key == "enter":
                Interface.Informações_do_usuario()
                break
            elif key == "esc":
                print("\nIndo para o menu anonimamente \nSeus dados estarão em branco")
                time.sleep(5)
                break

    def Informações_do_usuario():
        os.system('cls')
        print("Informe seus dados ou pressione enter para prosseguir")
        
        name = input(f"Nome: {cliente.usuario}\n").strip()
        cpf = input("CPF: ")
        nascimento = input("Nascimento: ")


           




os.system('cls')
cliente = Cliente()
interface = Interface()

print("Iniciando Sistema Bancario")
time.sleep(2)


interface.Criar_usuario()
interface.Menu()

print("\nSaindo do sistema")
time.sleep(2)
os.system('cls')