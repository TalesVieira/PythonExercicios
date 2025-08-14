#Um professor quer sortear um dos seus quatro alunos para apagar o quadro, faça um programa que ajude ele, lendo o nome
#dos alunos e escrevendo o nome do escolhido

import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

listaDeAlunos = [aluno1, aluno2, aluno3, aluno4]

alunoEscolhido = random.choice(listaDeAlunos)
print(f'O aluno escolhido foi {alunoEscolhido}')
