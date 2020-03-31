from os import system

system('title Gerenciador de Desafios')
system('mode 45,30')
op = 0
while op != 3:
    system('cls')
    print("""
    \t---------------------------
    \t      MENU PRINCIPAL
    \t---------------------------
    \t [1] Clonar Desafio
    \t [2] Deletar Desafios
    \t [3] Encerrar Programa
    \t---------------------------""")
    op = int(input('\tDigite uma opcao: '))
    if op == 1:
        # Clonar Desafio:
        original = int(input('\n\tDigite o Desafio a ser clonado: '))
        fim = int(input('\n\tDigite o Desafio final: '))
        for i in range(original + 1, fim + 1):
            system('copy Desafio{}.py Desafio{}.py'.format(str(original), str(i)))
        print('\n\tDesafio Clonado com Sucesso\n')
        system('pause')
    elif op == 2:
        # Deletar Desafio:
        inicio = int(input('\n\tDigite o Desafio inicial: '))
        fim = int(input('\n\tDigite o Desafio final: '))
        for i in range(inicio, fim + 1):
            system('del Desafio{}.py'.format(str(i)))
        print('\n\tDesafios Deletados com Sucesso\n')
        system('pause')
    elif op != 3:
        print('\n\tOpcao Invalida\n')
        system('pause')
else:
    exit

system('pause')
