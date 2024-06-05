import os
import time

class Banco:
    def __init__(self) -> None:
        pass

    def Saque(self):
        pass

    def Deposito(self):
        pass

class Cliente(Banco):
    def __init__(self):
        self.usuario = "Anonimo"
        self.CPF = "000.000.000-00"
        self.nascimento = "00/00/0000"
        self.saldo = 0.00


    def Deposito(self):
        print("\nComeçando operação de deposito")
        time.sleep(3)

        while True:
            os.system('cls')
            deposito = input(f"Saldo: R$ {self.saldo:.2f} \nQuanto quer depositar? \n--> ")

            if deposito == "": break

            try:
                deposito = float(deposito)
                if deposito > 0:
                    self.saldo += deposito
                    break
                else:
                    print("Deposito precisa ser maior que 0")
                    time.sleep(3)
            except:
                print("\nValor invalido! \nretomando operação")

        return print(f"Deposito de R$ {deposito:.2f} realizado com sucesso!")


    def Saque(self):
        print("\nComeçando operação de Saque")
        time.sleep(3)

        while True:
            os.system('cls')
            saque = input(f"Saldo: R$ {self.saldo:.2f} \nQuanto quer sacar: \n--> ")
                
            if saque == "": break

            try:
                saque = float(saque)
                if saque >= 0 and saque <= self.saldo:
                    self.saldo -= saque
                    break
                else:
                    print("\nSaldo insuficiente")
            except: 
                print("\nValor invalido! \nretomando operação")
                time.sleep(3)

        return print(f"\nSaque de R$ {saque:.2f} realizado com sucesso!")
    

    def Perfil(self):
        os.system('cls')
        print("\nPerfil do cliente")
        time.sleep(2)
        print(f"Nome: {self.usuario}")
        print(f"CPF: {self.CPF}")
        print(f"Nascimento: {self.nascimento}")
        print(f"Saldo: R$ {self.saldo:.2f}")
        time.sleep(2)

        while True:
            opcao = input(f"\nDeseja alterar o seu perfil? \n1 - Sim \n2 - Não \n--> ")


class Interface:
    def Menu():
        while True:
            os.system('cls')
            print("Bem vindo, " + cliente.usuario)
            print(f"\nSelecione uma opção"
                f"\n1 - Realizar deposito"
                f"\n2 - Realizar saque"
                f"\nenter - Sair")
            opcao = input("--> ")
            
            if opcao == "": break
            elif opcao == "1": cliente.Deposito()
            elif opcao == "2": cliente.Saque()
            else: print("Opção invalida")
            time.sleep(4)

    def Criar_usuario():
        os.system('cls')
        print("Deseja criar um novo usuario ou prosseguir anônimo? \n1 - Sim \n2 - Não")
        time.sleep(2)

        while True:
            #fazer seleção para:
            #criar o usuario
            #proseguir anonimo
            #corrigir erros



os.system('cls')
cliente = Cliente()
interface = Interface()

print("Iniciando Sistema Bancario")
time.sleep(2)


interface.Menu()

print("\nSaindo do sistema")
time.sleep(2)
os.system('cls')