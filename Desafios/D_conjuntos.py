import os
matematica = set()
contabilidade = set()


#registo da matematica      %----------------------------------------%
os.system('cls')
print("Matricula dos alunos de Matemática, enter para sair")
repit = 0

while repit < 150:
    aluno = input(f"aluno {repit+1}: ")
    if aluno == "":  
        repit += 150
    else:
        matematica.add(aluno)
        repit += 1


#registro da contabilidade  %----------------------------------------%
os.system('cls')
print("Matricula dos alunos de Contabilidade, enter para sair")
repit = 0

while repit < 100:
    aluno = input(f"aluno {repit+1}: ")
    if aluno == "":  
        repit += 100
    else:
        contabilidade.add(aluno)
        repit += 1


if matematica.intersection(contabilidade):
    repetidos = matematica.intersection(contabilidade)
else:
    repetidos = "não há alunos nas duas disciplinas simultaneamente"


#saida dos reistros         %----------------------------------------%
os.system('cls')
print("-----------------------------------------------")
print("alunos da matematica:\n", matematica, "\n\nalunos da contabilidade:\n", contabilidade)
print(f"\nalunos presente nas duas: \n{repetidos}")
print("-----------------------------------------------")