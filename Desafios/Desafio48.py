soma = 0
cont = 0
for i in range(1, 501):
    if (i % 2 != 0) and (i % 3 == 0):
        soma += i
        cont += 1
print('\n\tA soma dos {} valores = {}'.format(cont, soma))

input('\n\nPressione <enter> para continuar')
