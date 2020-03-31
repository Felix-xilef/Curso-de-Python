from os import system

n1 = int(input('\n\tDigite o 1° valor inteiro: '))
n2 = int(input('\tDigite o 2° valor inteiro: '))
if n1 > n2:
    print('\n\tO 1° valor é maior!\n')
elif n2 > n1:
    print('\n\tO 2° valor é maior!\n')
else:
    print('\n\tNão existe valor maior, os dois valores são iguais!\n')

system('pause')
