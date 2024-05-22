lista_completa = set(["Caio", "Davi", "Edmilson", "Erick", "Esmael", "Alison", 'Expedito', 'Armando', 'Kauã', 'Marcos', 'Graziel', "Raiane", "Natanael", "Gabriel", "Pedro", "Silas"])
equipe_1 = []
equipe_2 = []
equipe_3 = []
equipe_4 = []

for i in range(4):
    equipe_1.append(lista_completa.pop())
    equipe_2.append(lista_completa.pop())
    equipe_3.append(lista_completa.pop())
    equipe_4.append(lista_completa.pop())

print(f"equipe 1: \n {equipe_1} \nGerente: {equipe_1.pop()}\n\n equipe 2: \n {equipe_2} \nGerente: {equipe_2.pop()}\n")
print(f"equipe 3: \n {equipe_3} \nGerente: {equipe_3.pop()}\n\n equipe 4: \n {equipe_4} \nGerente: {equipe_4.pop()}\n\n")