from os import system

n1 = int(input('\n\tDigite o 1° número: '))
n2 = int(input('\tDigite o 2° número: '))
n3 = int(input('\tDigite o 3° número: '))
if n1 > n2:
    if n1 > n3:
        maior = n1
elif n1 < n3:
    menor = n1
if n2 > n1:
    if n2 > n3:
        maior = n2
elif n2 < n3:
    menor = n2
if n3 > n1:
    if n3 > n2:
        maior = n3
elif n3 < n2:
    menor = n3
print('\n\tMaior número = {}\n\tMenor número = {}\n'.format(maior, menor))

system('pause')
