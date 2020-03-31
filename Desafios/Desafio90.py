aluno = dict()
aluno['nome'] = input('\n\tDigite o nome do(a) aluno(a): ').strip().capitalize()
aluno['média'] = float(input('\tDigite a média do(a) aluno(a): '))
aluno['situação'] = 'Aprovado(a)' if aluno['média'] >= 7 else 'Reprovado(a)'
print(f'\n\t{aluno["nome"]} ficou com média {aluno["média"]} e foi {aluno["situação"]}')

input('\n\nPressione <enter> para continuar')
