# def função(* parâmetro) - o asterisco (*) significa que é um parâmetro empacotado, isto é, não se sabe quantos parâmetros serão recebidos
#                           portanto é criado uma tupla com os parâmetros passados
def contador(* num):
    for i in num:
        print(i)
    print(f'Recebi os valores e são {len(num)}')


# Programa Principal

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

input('\n\nPressione <enter> para continuar')
