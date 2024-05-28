import os
os.system('cls')
saldo = 1500
saldo = float(saldo)
extrato = []

def Menu():
    os.system('cls')
    print(texto)
    opcao = input("o que deseja fazer: \n1 - Sacar \n2 - Depositar \n3 - Visualizar Extrato \n--> ")
    return opcao


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
    input("\nPressione Enter para continuar...")
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
        print("\nValor inválidoo!")
    input("\nPressione Enter para continuar...")
    return saldo


def Extrato():
    os.system('cls')
    print(texto, "\n")
    for operacao in extrato:
        print(operacao)
    input("\nPressione Enter para continuar...")



texto = "        === Sistema Bancário === \n"
print(texto)
input("\nPressione Enter para continuar ou sair...")

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

print("\nFechando Programa...\n\n")