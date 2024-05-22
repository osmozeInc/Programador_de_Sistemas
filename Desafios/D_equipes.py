import random
equipes = [['Raiane', 'Felipe', 'Caio', 'Kauã'],
            ['Pedro', 'Expedito', 'Alison', 'Silas'],
              ['Esmael', 'Armando', 'Natanael', 'Erick'],
                ['Davi', 'Marcos', 'Gabriel', 'Graziel']]
 

for i in range(4): print(f"equipe {i+1}: \n {equipes[i]} \nGerente: {random.choice(equipes[i])
}\n")