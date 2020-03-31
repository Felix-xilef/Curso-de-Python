# num = (2, 5, 9, 1) - Tupla
num = [2, 5, 9, 1] # Lista (como uma tupla porém mutável)

print(f'\n\tnum = {num}\n\ttamanho = {len(num)}')

num[2] = 3

print(f'\n\tnum = {num}\n\ttamanho = {len(num)}')

num.append(7) # .append(x) - adiciona elemento x na última posição

print(f'\n\tnum = {num}\n\ttamanho = {len(num)}')

num.sort()

print(f'\n\tnum = {num}\n\ttamanho = {len(num)}')

num.sort(reverse=True)

print(f'\n\tnum = {num}\n\ttamanho = {len(num)}')

num.insert(2, 0) # .insert(x, y) - insere o valor y na posição x (mantendo valores da lista)

print(f'\n\tnum = {num}\n\ttamanho = {len(num)}')

num.pop() # .pop(x) - remove elemento que está na posição x (se x = NULL remove último elemento)

print(f'\n\tnum = {num}\n\ttamanho = {len(num)}')

num.pop(2)

print(f'\n\tnum = {num}\n\ttamanho = {len(num)}')

num.insert(2, 2)

print(f'\n\tnum = {num}\n\ttamanho = {len(num)}')

num.remove(2) # .remove(x) - remove o primeiro elemento x encontrado na lista

print(f'\n\tnum = {num}\n\ttamanho = {len(num)}')

input('\n\nPressione <enter> para continuar')
