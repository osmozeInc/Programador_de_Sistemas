import keyboard
import time
import os
import sys

class Students:
    lista_de_nomes = []
    nomes_registrados = False
    equipes = [[]]

    def Adicionar_nomes(self):
        os.system('cls')
        print("Adicione um nome ou nada para sair\n")

        while True:
            nome = input("Nome: ").strip().title()
            if nome == "": break
            self.lista_de_nomes.append(nome)
        self.Salvar_lista()
    
    def Salvar_lista(self):
        os.system('cls')
        print("nomes na lista:\n", self.lista_de_nomes)
        print("\nSalvar? (enter)"
              "\nCancelar (esc)")
        while True:
            key = keyboard.read_event()
            if key.event_type == "down":
                if key.name == "enter":
                    try:
                        with open("nomes.txt", "w") as arquivo:
                            for nome in self.lista_de_nomes:
                                arquivo.write(nome + "\n")
                            print("\nNomes salvos")
                            input()
                        break
                    except IOError as e:
                        print(f"Erro ao salvar nomes: {e}")

                elif key.name == "esc":
                    print("Cancelando")
                    self.lista_de_nomes.clear()
                    break
        time.sleep(3)

    def Ver_nomes(self):
        os.system('cls')
        try:
            with open("nomes.txt", "r") as file:
                nomes = file.readlines()
                for i, nome in enumerate(nomes, start=1):
                    print(f" {i}. {nome}", end="")
        except FileNotFoundError:
            print("Não há nomes salvos")
        input("\nPressione enter para continuar")

    def Limpar_lista(self):
        os.system('cls')
        print("Todos os nomes serão apagados")
        print("Tem certeza? (enter) ou (esc)")
        while True:
            key = keyboard.read_event()
            if key.event_type == "down":
                if key.name == "enter":
                    os.remove("nomes.txt")
                    print("Lista limpa")
                    input()
                    break
                elif key.name == "esc":
                    print("Cancelando")
                    break
        time.sleep(3)

    def Montar_equipes(self):
        print("Montando equipes\n")
        time.sleep(2)

        if os.path.exists("equipes.txt"):
            print("ja existem 4 equipes formadas\n"
                    "limpe a lista de nomes e tente novamente")
            input("\nPressione enter para continuar")
            return
        
        if not os.path.exists("nomes.txt"):
            print("Não há nomes salvos")
            input("\nPressione enter para continuar")
            return
        
        with open("nomes.txt", "r") as file:
            lista_equipes = []
            for nome in file:
                lista_equipes.append((nome).strip())

            while True:
                try:
                    numero_equipes = int(input("Quantas equipes deseja formar? "))
                    break
                except:
                    print("Digite um número inteiro")

            for i in range(numero_equipes):
                remover_nomes = []
                for nome in lista_equipes:
                    os.system('cls')

                    print(f"Adicionar {(nome)} a equipe {len(self.equipes)}?"
                        "\nenter - fechar equipe"
                        "\n1 - sim"
                        "\n2 - não")
                    adicionar = input("--> ")

                    if adicionar == "1":
                        self.equipes[len(self.equipes)-1].append(nome)
                        remover_nomes.append(nome)
                        print(f"{nome} adicionado")
                        time.sleep(1.2)

                    elif adicionar == "2":
                        print(f"{nome} não adicionado")
                        time.sleep(1.2)

                    elif adicionar == "":
                        self.equipes.append([])
                        for remocao in remover_nomes:
                            lista_equipes.remove(remocao)
                        break

                    else:
                        print("Opção inválida")
                        time.sleep(1.5)

                    if len(self.equipes[len(self.equipes)-1]) == 4:
                        print("Equipe completa")
                        if len(lista_equipes) >= 1: self.equipes.append([])
                        for remocao in remover_nomes:
                            lista_equipes.remove(remocao)
                        time.sleep(1.5)
                        break

                    if len(self.equipes[len(self.equipes)-1]) == len(lista_equipes):
                        print("Equipes fechadas")
                        for remocao in remover_nomes:
                            lista_equipes.remove(remocao)
                        time.sleep(1.5)
                        break

        self.Salvar_equipes()

    def Salvar_equipes(self):
        print("Salvar equipes? (enter) ou (esc)")
        while True:
            key = keyboard.read_event()
            if key.event_type == "down":
                if key.name == "enter":
                    try:
                        with open("equipes.txt", "w") as file:
                            for i, equipe in enumerate(self.equipes, start=1):
                                file.write(f"\nEquipe {i}: ")
                                for nome in equipe:
                                    file.write(nome + ", ")
                        print("Equipes salvas")
                        input()
                    except IOError as e:
                        print(f"Erro ao salvar equipes: {e}")
                    break
                elif key.name == "esc":
                    print("Cancelando")
                    break
        time.sleep(2)

    def Ver_equipes(self):
        os.system('cls')
        try:
            with open("equipes.txt", "r") as file:
                for equipe in file:
                    print(equipe)
        except FileNotFoundError:
            print("Não há equipes salvas")
        input("\nPressione enter para continuar")

    def Limpar_equipes(self):
        os.system('cls')
        print("Todos as equipes serão apagadas")
        print("Tem certeza? (enter) ou (esc)")
        while True:
            key = keyboard.read_event()
            if key.event_type == "down":
                if key.name == "enter":
                    try:
                        os.remove("equipes.txt")
                        print("Lista limpa")
                        input()
                    except FileNotFoundError:
                        print("Não há equipes salvas")
                        input()
                    break
                elif key.name == "esc":
                    print("Cancelando")
                    break
        time.sleep(3)


def Menu():
    while True:
        os.system('cls')
        print("Selecione uma opção"
              "\n----------------------"
              "\n1 - Adicionar nomes"
              "\n2 - Ver nomes salvos"
              "\n3 - Limpar lista"
              "\n4 - Montar equipes"
              "\n5 - Ver equipes"
              "\n6 - limpar equipes"
              "\nenter - Sair")
        
        opcao = input("--> ")
        if opcao == "": break
        elif opcao == "1": students.Adicionar_nomes()
        elif opcao == "2": students.Ver_nomes()
        elif opcao == "3": students.Limpar_lista()
        elif opcao == "4": students.Montar_equipes()
        elif opcao == "5": students.Ver_equipes()
        elif opcao == "6": students.Limpar_equipes()


students = Students()
Menu()