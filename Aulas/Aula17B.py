valores = [] # ou valores = list()

# valores.append(5)
# valores.append(9)
# valores.append(4)

for i in range(0, 5):
    valores.append(int(input('\tDigite um valor: ')))

for c, i in enumerate(valores):
    print(f'\n\tNa posição {c} encontrei o valor {i}!', end='')
print('\n\n\tCheguei ao final da lista')

input('\n\nPressione <enter> para continuar')
