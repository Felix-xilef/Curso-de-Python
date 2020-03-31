from os import system

n1 = float(input('\n\tDigite a nota 1: '))
n2 = float(input('\tDigite a nota 2: '))
media = (n1 + n2)/2
print('\n\tMédia = {:.2f}'.format(media))
if media < 5:
    print('\n\tAluno REPROVADO!\n')
elif media >= 7:
    print('\n\tAluno APROVADO!\n')
else:
    print('\n\tAluno de RECUPERAÇÃO!\n')

system('pause')
