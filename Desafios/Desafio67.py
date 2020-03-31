from os import system

system('title Tabuadas')
while True:
    system('cls')
    n = int(input("""
    \t +------------------------------------+
    \t |        Programa de Tabuadas        |
    \t +------------------------------------+
    \t   Digite um número inteiro (negativo
    \t   para encerrar): """))
    if n < 0:
        break
    print('\t +------------------------------------+')
    for i in range(1, 11):
        print(f'\t |{n:>13} x {i:<2} = {n * i:<15}|')
    print('\t +------------------------------------+')
    system('pause')

system('pause')
# input('\n\nPressione <enter> para continuar')
