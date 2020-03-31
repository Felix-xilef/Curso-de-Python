from os import system

inicio = int(input('\n\tDigite o início: '))
fim = int(input('\n\tDigite o fim: '))
passo = int(input('\n\tDigite o passo: '))
print('\n')
for i in range(inicio, fim + 1, passo):
    print('\t{}'.format(i))
print('\n\tFIM\n')

s = 0
for i in range(0, 4):
    n = int(input('\tDigite um número: '))
    s += n
print('\n\tSomatório de todos os valores = {}\n\tFIM\n'.format(s))

system('pause')
