numero = int(input('\n\tDigite um número inteiro qualquer: '))

# for
fatorial = 1
print('\tFatorial de {0}:\n\t{0}! = '.format(numero), end='')
for i in range(numero, 1, -1):
    fatorial *= i
    print('{} x '.format(i), end='')
print('1 = {}'.format(fatorial))

# while
fatorial = 1
print('\tFatorial de {0}:\n\t{0}! = '.format(numero), end='')
i = numero
while i > 1:
    fatorial *= i
    print('{} x '.format(i), end='')
    i -= 1
print('1 = {}'.format(fatorial))


input('\n\nPressione <enter> para continuar')
