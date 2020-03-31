# Tupla - (declaração com ou sem parênteses) como um array porém imutável e podem ter dados de diferentes tipos
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'

print(lanche)
print(lanche[1])
print(lanche[-2]) # indices negativos começam do último elemento e terminam no primeiro
print(lanche[1:3]) # tupla[x:y] - a partir do elemento x até y - 1
print(lanche[:2])  # *caso x = NULL desde o começo
print(lanche[2:])  # *caso y = NULL até o final
print(lanche[-2:])
print(sorted(lanche)) # sorted - retorna os elementos em ordem (alfabetica, numérica)

for i in range(0, len(lanche)):
    print(f'\n\tVou comer {lanche[i]} na posição {i}', end='')

for i, j in enumerate(lanche):
    print(f'\n\tVou comer {j} na posição {i}', end='')

for i in lanche:
    print(f'\n\tVou comer {i}', end='')

print('\n\n\tComi pra caramba!')

input('\n\nPressione <enter> para continuar')
