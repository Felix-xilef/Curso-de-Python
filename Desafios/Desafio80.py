valores = list()
for i in range(0, 5):
    aux = int(input('\tDigite um número inteiro: '))
    if i == 0 or valores[-1] <= aux:
        valores.append(aux)
    else:
        for j in range(0, i):
            if valores[j] >= aux:
                valores.insert(j, aux)
                break

print(f'\n\t{valores}')

input('\n\nPressione <enter> para continuar')
