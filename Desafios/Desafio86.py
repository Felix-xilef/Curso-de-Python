from auxiliar import receberInt

matriz = [[], [], []]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(receberInt())

for i in range(0, 3):
    print(f'\n\t+{"-" * 17}+', end='\n\t')
    for j in range(0, 3):
        print(f'|{matriz[i][j]:^5}', end='')
    print('|' if i < 2 else f'|\n\t+{"-" * 17}+', end='')

input('\n\nPressione <enter> para continuar')
