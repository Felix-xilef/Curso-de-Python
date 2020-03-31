soma = 0
pares = 0
print('\n')
for i in range(1, 7):
    n = int(input('\tDigite o {}° número inteiro: '.format(i)))
    if n % 2 == 0:
        soma += n
        pares += 1
print('\n\tSoma dos {} números pares digitados = {}'.format(pares, soma))

input('\n\nPressione <enter> para continuar')
