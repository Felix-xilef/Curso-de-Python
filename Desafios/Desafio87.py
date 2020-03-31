from auxiliar import receberInt

matriz = [[], [], []]
somaPares = soma3C = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(receberInt())
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]

for i in range(0, 3):
    if matriz[1][i] > maior or i == 0:
        maior = matriz[1][i]
    soma3C += matriz[i][2]

for i in range(0, 3):
    print(f'\n\t+{"-" * 17}+', end='\n\t')
    for j in range(0, 3):
        print(f'|{matriz[i][j]:^5}', end='')
    print('|' if i < 2 else f'|\n\t+{"-" * 17}+', end='')

print(f'\n\tSoma dos pares = {somaPares}\n\tSoma da 3° coluna = {soma3C}\n\tMaior valor da 2° linha = {maior}')

input('\n\nPressione <enter> para continuar')
