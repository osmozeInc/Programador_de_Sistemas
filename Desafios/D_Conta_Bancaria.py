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
        self.usuario = "Francisco"
        self.saldo = 0.00

    def Deposito(self):
        print("Começando operação de deposito")
        time.sleep(3)

        while True:
            os.system('cls')
            deposito = input(f"Saldo: R$ {self.saldo:.2f} \nQuanto quer depositar? \n--> ")

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

        return print(f"Deposito de R$ {self.saldo:.2f} realizado com sucesso!")


    def Saque(self):
        print("Começando operação de Saque")
        time.sleep(3)

        while True:
            os.system('cls')
            saque = input(f"Saldo: R$ {self.saldo:.2f} \nQuanto quer sacar: \n--> ")
                
            try:
                saque = float(saque)
                if saque >= 0 and saque <= self.saldo:
                    self.saldo -= saque
                    break
                else:
                    print("Saldo insuficiente")
            except: 
                print("\nValor invalido! \nretomando operação")
                time.sleep(3)

        return print(f"Saque de R$ {self.saldo:.2f} realizado com sucesso!")
    

os.system('cls')
cliente = Cliente()
cliente.Deposito()
cliente.Saque()