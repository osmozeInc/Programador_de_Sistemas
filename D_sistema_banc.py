import sys
import os
import time
os.system('cls')
texto = "        === Sistema Bancário === \n"
saldo = float(1500)
extrato = []

def Menu():
    os.system('cls')
    print(texto)
    opcao = input("o que deseja fazer: \n1 - Sacar \n2 - Depositar \n3 - Visualizar Extrato \n--> ")
    return opcao

def Carregando():
    for ponto in ['.', '.', '.', '.']:
        time.sleep(0.5)
        sys.stdout.write(ponto)
        sys.stdout.flush()

def Retornando():
    for tempo in ['(5)', '(4)', '(3)', '(2)', '(1)', '(0)', ]:
        sys.stdout.write(tempo)
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write('\b' * 3)
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
    print(texto, "\n")
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




#
#                            Explicação Detalhada

#  O código importa o módulo os e usa os.system('cls') para limpar a tela no Windows.
#  import os
#  os.system('cls')

#       Variáveis Globais:
#  Inicializa o saldo com 1500, convertendo-o para float, e cria uma lista vazia para armazenar o extrato das operações.

#       Função Menu:
#  Limpa a tela, exibe o texto de saldo, solicita a escolha do usuário e retorna essa escolha.

#       Função Saque:
#  Limpa a tela, exibe o texto de saldo, solicita o valor do saque e tenta convertê-lo para float.
#  Se o valor for válido e menor ou igual ao saldo, realiza o saque, atualiza o saldo e adiciona a operação ao extrato.
#  Se o valor for inválido ou maior que o saldo, exibe uma mensagem de erro.
#  Retorna o saldo atualizado.

#       Função Deposito:
#  Limpa a tela, exibe o texto de saldo, solicita o valor do depósito e tenta convertê-lo para float.
#  Se o valor for válido e positivo, realiza o depósito, atualiza o saldo e adiciona a operação ao extrato.
#  Se o valor for inválido ou negativo, exibe uma mensagem de erro.
#  Retorna o saldo atualizado.

#       Função Extrato:
#  Limpa a tela, exibe o texto de saldo e todas as operações armazenadas no extrato.

#       Loop Principal:
#  Inicializa o texto de boas-vindas e espera o usuário pressionar Enter para continuar.
#  Entra em um loop infinito, atualizando e exibindo o saldo após cada operação.
#  Chama a função Menu para obter a escolha do usuário.
#  Dependendo da escolha, chama as funções Saque, Deposito ou Extrato.
#  Sai do loop e imprime uma mensagem de encerramento se a escolha for uma string vazia.
#
#       try-except: 
#  Permite capturar e tratar erros que ocorrem durante a execução do código,
#  prevenindo que o programa falhe inesperadamente e proporcionando uma maneira controlada de lidar com erros.

#       while True: 
#  Cria um loop infinito que continuará até que uma condição de saída (break) seja encontrada,
#  permitindo que o programa permaneça em execução até que o usuário decida sair.
