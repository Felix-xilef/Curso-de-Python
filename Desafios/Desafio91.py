from random import randint
from operator import itemgetter

jogadas = {}
for i in range(1, 5):
    jogadas[f'jogador {i}'] = randint(1, 6)

print(jogadas)

# Colocando em ordem - Aula
jogadas = sorted(jogadas.items(), key = itemgetter(1), reverse=True) # sorted() retorna uma lista
# key = itemgetter(x) - colocar por quais valores o dicionário será colocado em ordem (0 - key/1 - value)
# Fim

# Colocando dicionário em ordem - Felix
# auxK = list(jogadas.copy().keys())
# auxV = list(jogadas.copy().values())
# jogadas.clear()
# for i in range(0, len(auxV)):
#     for j in range(i, 0, -1):
#         if auxV[j] > auxV[j - 1]:
#             auxV.insert(j - 1, auxV[j])
#             auxV.pop(j + 1)
#             auxK.insert(j - 1, auxK[j])
#             auxK.pop(j + 1)
#         else:
#             break
# 
# for i in range(0, len(auxK)):
#     jogadas[auxK[i]] = auxV[i]
# Fim

print(jogadas)

input('\n\nPressione <enter> para continuar')
