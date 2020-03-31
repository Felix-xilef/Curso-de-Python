galera = list()

dado = list()
for i in range(0, 3):
    dado.append(input('\n\tNome: '))
    dado.append(int(input('\tIdade: ')))
    galera.append(dado[:])
    dado.clear()

for i in range(0, 3):
    nome = input('\n\tNome: ')
    idade = int(input('\tIdade: '))
    galera.append([nome, idade])

print(galera)

for i in galera:
    if i[1] >= 21:
        print(i[0])

input('\n\nPressione <enter> para continuar')
