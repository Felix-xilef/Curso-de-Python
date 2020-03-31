valores = (int(input('\tDigite o 1° número inteiro: '))), (int(input('\tDigite o 2° número inteiro: '))), (int(input('\tDigite o 3° número inteiro: '))), (int(input('\tDigite o 4° número inteiro: ')))
if 9 in valores:
    aux9 = valores.count(9)
else:
    aux9 = 0
if 3 in valores:
    aux3 = f'Posição do primeiro número 3 = {valores.index(3) + 1}°'
else:
    aux3 = 'O número 3 não apareceu'
print(f'\n\tQuantidade de vezes que apareceu o número 9 = {aux9}\n\t{aux3}\n\tValores pares:', end='')
for i in valores:
    if i % 2 == 0:
        print(f'\t{i}', end='')

input('\n\nPressione <enter> para continuar')

