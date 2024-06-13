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
        self.Savar_lista()
    
    def Savar_lista(self):
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
                    with open("nomes.txt", "w") as arquivo:
                        arquivo.write("")
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

        with open("nomes.txt", "r") as file:
            lista_equipes = []
            for nome in file:
                lista_equipes.append((nome).strip())
            for i in range(0, 4):
                j = 0
                while j < 4:
                    for nome in lista_equipes:
                        os.system('cls')
                        print(f"Adicionar {(nome)} a equipe {i+1}?"
                            "\nenter - fechar equipe"
                            "\n1 - sim"
                            "\n2 - não")
                        adicionar = input("--> ")

                        if adicionar == "1":
                            self.equipes[i].append(nome)
                            lista_equipes.remove(nome)
                            print(f"{nome} adicionado")
                            time.sleep(1.2)

                        elif adicionar == "2":
                            print(f"{nome} não adicionado")
                            time.sleep(1.2)

                        elif adicionar == "":
                            self.equipes.append([])
                            i += 1
                            break

                        else:
                            print("Opção inválida")
                            time.sleep(1.5)

        self.Salvar_equipes()

    def Salvar_equipes(self):
        input("Salvar equipes? (enter) ou (esc)")
        try:
            with open("equipes.txt", "w") as file:
                for i, equipe in enumerate(self.equipes, start=1):
                    file.write(f"Equipe {i}")
                    for nome in equipe:
                        file.write(f"{nome}")
            print("Equipes salvas")
            input()
        except IOError as e:
            print(f"Erro ao salvar equipes: {e}")

    def Ver_equipes(self):
        try:
            with open("equipes.txt", "r") as file:
                for equipe in file:
                    print(equipe)
        except FileNotFoundError:
            print("Não há equipes salvas")
        input("\nPressione enter para continuar")


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
              "\nenter - Sair")
        
        opcao = input("--> ")
        if opcao == "": break
        elif opcao == "1": students.Adicionar_nomes()
        elif opcao == "2": students.Ver_nomes()
        elif opcao == "3": students.Limpar_lista()
        elif opcao == "4": students.Montar_equipes()
        elif opcao == "5": students.Ver_equipes()
        

    


students = Students()
Menu()