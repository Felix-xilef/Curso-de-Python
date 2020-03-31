def maior(*valores):
    print(('=~' * 30) + '=')
    print(f'Valores informados: {valores}\nQuantidade = {len(valores)}\nMaior valor = {max(valores)}')
    print(('=~' * 30) + '=')


# main
maior(1, 5, 4, 10, 2)
maior(5, 0, 0, 1, 4, 70, 70, 70, 69)

input('\n\nPressione <enter> para continuar')
