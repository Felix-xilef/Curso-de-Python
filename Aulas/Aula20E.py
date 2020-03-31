def dobra(lst):
    for i in range(0, len(lst)):
        lst[i] *= 2 # como é pasado uma lista toda alteração feita na lst alterará a principal


# Main
valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)

input('\n\nPressione <enter> para continuar')
