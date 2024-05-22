lista_completa = set(["Caio", "Davi", "Edmilson", "Erick", "Esmael", "Alison", 'Expedito', 'Armando', 'Kauã', 'Marcos', 'Graziel', "Raiane", "Natanael", "Gabriel", "Pedro", "Silas"])
equipes = [[], [], [], []]

for i in range(4):
        for j in range(4):
            equipes[i].append(lista_completa.pop()) 

for i in range(4): print(f"equipe {i+1}: \n {equipes[i]} \nGerente: {equipes[i].pop()}\n")