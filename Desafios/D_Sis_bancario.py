import os
os.system('cls')
saldo = 1500
extrato = []

input("Sistema Bancário \npressione enter para prosseguir ou sair\n")
escolha = input("o que deseja fazer: \n1 - Sacar \n2 - Depositar \n3 - Visualizar Extrato \n--> ")

while True:

    if str(escolha) == "": break


    elif int(escolha) == 1:
        os.system('cls')
        saque = float(input(f"Extrato: R$ {saldo:.2f} \nqual o valor do saque?\n --> "))
        os.system('cls')
        if saldo >= saque and saque > 0: 
            print(f"sacando: R$ {saque:.2f} \nExtrato atual: R$ {(saldo - saque):.2f}")
            extrato.append(f"sacado o valor de R$ {saque}")
            saldo = saldo - saque
        else: print(f"Saldo Insuficiente \nSaldo: R$ {saldo:.2f}")
        escolha = input("\n\no que deseja fazer: \n1 - Sacar \n2 - Depositar \n3 - Visualizar Extrato \n--> ")


    elif int(escolha) == 2:
        os.system('cls')
        deposito = float(input(f"Extrato: R$ {saldo:.2f} \nqual o valor do deposito?\n --> "))
        os.system('cls')
        print(f"Depositando R$ {deposito:.2f} \nExtrato atual: R$ {(deposito + saldo):.2f}")
        extrato.append(f"depositado o valor de R$ {deposito:.2f}\n")
        saldo = deposito + saldo
        escolha = input("\n\no que deseja fazer: \n1 - Sacar \n2 - Depositar \n3 - Visualizar Extrato \n--> ")


    elif int(escolha) == 3:
        os.system('cls')
        print(f"Saldo atual: R$ {saldo:.2f}\n")
        for operacao in extrato:
            print(operacao)
        escolha = input("\n\no que deseja fazer: \n1 - Sacar \n2 - Depositar \n3 - Visualizar Extrato \n--> ")

        

    else:
        os.system('cls')
        print("Valor inválido")
        escolha = input("\no que deseja fazer: \n1 - Sacar \n2 - Depositar \n3 - Visualizar Extrato \n--> ")
os.system('cls')
print("\nFechando Sistema...\n\n")