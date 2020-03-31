a = [2, 3, 4, 7]
b = a # Quando se iguala uma lista a outra cria-se uma ligação entre ela, isto é, o que for alterado em uma será alterado na outra
b[2] = 8
print(f'\n\tLista a: {a}\n\tLista b: {b}')
c = a[:] # c = fatiamento de a começando do primeiro ao último elemento, isto é cria-se uma cópia de a em c (não é criada uma ligação)
c[2] = 4
print(f'\n\tLista a: {a}\n\tLista c: {c}')

input('\n\nPressione <enter> para continuar')
