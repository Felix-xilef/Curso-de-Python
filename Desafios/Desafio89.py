from os import system
from auxiliar import receberInt

system('title Administrador de Notas')
alunos = list()
notas = list()
while True:
    system('cls')
    op = receberInt(f"""
    \t +{'-' * 24}+
    \t | Administrador de Notas |
    \t +{'-' * 24}+
    \t | 1 - Adicionar aluno    |
    \t | 2 - Boletim geral      |
    \t | 3 - Boletim individual |
    \t | 4 - Encerrar           |
    \t +{'-' * 24}+
    \t   Digite uma opção: """)
    if op == 1:
        nome = input('\n\tDigite o nome do aluno: ').strip().lower()
        notas.append(float(input('\tDigite a nota 1: ')))
        notas.append(float(input('\tDigite a nota 2: ')))
        alunos.append([nome, notas[:]])
        notas.clear()
        print('\n\tAluno cadastrado com sucesso!')
    elif op == 2:
        print('\n\tMédias:')
        for i in alunos:
            print(f'\t\t{i[0]}: {(i[1][0] + i[1][1])/2}')     
    elif op == 3:
        nome = input('\n\tDigite o nome do aluno: ').strip().lower()
        alunoIndex = -1
        for i in alunos:
            if nome in i:
                alunoIndex = alunos.index(i)
                break
        if alunoIndex != -1:
            print(f'\n\t{alunos[alunoIndex][0]}:\n\t\tNota 1 = {alunos[alunoIndex][1][0]}\n\t\tNota 2 = {alunos[alunoIndex][1][1]}\n\tMédia = {(alunos[alunoIndex][1][0] + alunos[alunoIndex][1][1])/2}')
        else:
            print('\n\t!!! Aluno não encontrado !!!')
    elif op == 4:
        break
    else:
        print('\t!!! Resposta Inválida !!!')
    print('\n')
    system('pause')

print('\n')
system('pause') # input('\n\nPressione <enter> para continuar')
