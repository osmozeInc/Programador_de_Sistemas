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
        return 

    def Saque(self):
        print("Começando operação de Saque")
        time.sleep(3)

        while True:
            os.system('cls')
            saque = input(f"Saldo: R$ {self.saldo:.2f} \nQuanto quer sacar:")
                
            if saque == float(saque):
                if saque >= 0 and saque <= self.saldo:
                    saldo = saldo - saque
                    print(f"Saque de R$ {saldo} realizado com sucesso!")
                    break
                else:
                    print("Saldo insuficiente")
            else: 
                print("Valor invalido")
                time.sleep(3)

        return print(f"Saque de R$ {saldo} realizado com sucesso!")
    


os.system('cls')
cliente = Cliente()
cliente.Saque()