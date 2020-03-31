# n = s = 0
# while n != 999:
#     n = int(input('\tDigite um número: '))
#     s += n

s = 0
while True:
    n = int(input('\tDigite um número: '))
    if n == 999:
        break # break interrompe o loop no qual está contido
    s += n

# print('\n\tA soma vale {}'.format(s))
print(f'\n\tA soma vale {s}') # nova forma (f string) -> colocar um f minusculo antes de abrir aspas, o valor pode ser colocado diretamente nas chaves

input('\n\nPressione <enter> para continuar')
