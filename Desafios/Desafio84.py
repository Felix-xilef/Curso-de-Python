from auxiliar import receberSN

pessoas = list()
while True:
    nome = input(f'\n\tDigite o nome da pessoa: ')
    peso = float(input('\tDigite o pesso em kg: '))
    pessoas.append([nome, peso])
    resp = receberSN()
    if resp == 'n':
        break

pesados = list()
leves = list()
for i in pessoas:
    if pessoas.index(i) == 0:
        pesados.append([i[0], i[1]])
        leves.append([i[0], i[1]])
    elif i[1] >= pesados[0][1]:
        if i[1] > pesados[0][1]:
            pesados.clear()
        pesados.append([i[0], i[1]])
    elif i[1] <= leves[0][1]:
        if i[1] < leves[0][1]:
            leves.clear()
        leves.append([i[0], i[1]])

print(f'\n\tQuantidade de pessoas cadastradas = {len(pessoas)}\n\tPessoas com {pesados[0][1]}kg: ', end='')
for i in pesados:
    print(f'{i[0]}  ', end='')
print(f'\n\tPessoas com {leves[0][1]}kg: ', end='')
for i in leves:
    print(f'{i[0]}  ', end='')

input('\n\nPressione <enter> para continuar')
