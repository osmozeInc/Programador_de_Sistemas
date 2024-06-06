import sys
import os
import time

os.system('cls')
texto = "        === Sistema Bancário === \n"
saldo = float(500)
extrato = []

def Menu():
    os.system('cls')
    print(texto)
    opcao = input("o que deseja fazer: \n1 - Sacar \n2 - Depositar \n3 - Visualizar Extrato \n--> ")
    return opcao

def Carregando():
    for ponto in ['.', '.', '.', '']:
        time.sleep(0.6)
        sys.stdout.write(ponto)
        sys.stdout.flush()

def Retornando():
    for tempo in range(8, 0, -1):
        sys.stdout.write(f"({tempo}s)")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('\b' * 4)
        sys.stdout.flush()

def Saque(saldo):
    os.system('cls')
    print(texto)
    valor = input("Qual o valor do saque?\n--> ")
    try:
        valor = float(valor)
        if valor <= saldo and valor > 0:
            saldo -= valor
            extrato.append(f"Sacado: R$ {valor:.2f}")
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.\nSaldo atual: R$ {saldo:.2f}")
        else:
            print("\nSaldo insuficiente!")
    except ValueError:
        print("\nValor inválido!")
    print("\nRetornando ao menu ", end='')
    Retornando()
    return saldo

def Deposito(saldo):
    os.system('cls')
    print(texto)
    valor = input("Qual o valor do deposito?\n--> ")
    try:
        valor = float(valor)
        if valor > 0:
            saldo += valor
            extrato.append(f"Depositado: R$ {valor:.2f}")
            print(f"\nDeposito de R$ {valor:.2f} realizado com sucesso.\nSaldo atual: R$ {saldo:.2f}")
        else: 
            print("\nValor inválido!")
    except:
        print("\nValor inválido!")
    print("\nRetornando ao menu ", end='')
    Retornando()
    return saldo

def Extrato():
    os.system('cls')
    print(texto, "\n\nExtrato:")
    for operacao in extrato:
        print(operacao)
    input("\nPressione Enter para continuar...")


print(texto)
time.sleep(0.5)
print("\nIniciando Sistema", end='')
Carregando()

while True:
    texto = f"Saldo: R$ {saldo:.2f}"
    escolha = Menu()

    if escolha == "": break

    elif escolha == '1':
        saldo = Saque(saldo)
        
    elif escolha == '2':
        saldo = Deposito(saldo)

    elif escolha == '3':
        Extrato()
    
    else: 
        print("Valor inválido!")
        input("\nPressione Enter para continuar...")

    texto = f"Saldo: R$ {saldo:.2f}"
os.system('cls')
print("Fechando Programa", end='')
Carregando()
print("\n\n")