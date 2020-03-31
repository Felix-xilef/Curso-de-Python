def soma(*valores):
    s = 0
    for i in valores:
        s += i
    print(f'Soma dos valores {valores} = {s}')


# Main
soma(5, 2)
soma(2, 9, 4)

input('\n\nPressione <enter> para continuar')
