n = -1
par = impar = 0
while n != 0:
    n = int(input('\tDigite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('\n\tQuantidade de Números digitados:\n\t\tPares = {}\n\t\tÍmpares = {}'.format(par, impar))

input('\n\nPressione <enter> para continuar')
