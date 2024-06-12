import keyboard
import time
import os
import sys

class Students:
    lista_de_nomes = []
    nomes_registrados = False

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
        try:
            with open("nomes.txt", "r") as file:
                x = 1
                for nome in file:
                    print(f" {x}. nome: {nome.strip()}")
                    x += 1
        except:
            print("Nenhum nome salvo")
            input("\nPressione enter para continuar")
        input("\nPressione enter para continuar")



def Menu():
    while True:
        os.system('cls')
        print("Selecione uma opção"
              "\n----------------------"
              "\n1 - Adicionar nomes"
              "\n2 - Ver nomes salvos"
              "\n3 - Montar equipes"
              "\nenter - Sair")
        
        opcao = input("--> ")
        if opcao == "": break
        elif opcao == "1": students.Adicionar_nomes()
        elif opcao == "2": students.Ver_nomes()

    


students = Students()
Menu()