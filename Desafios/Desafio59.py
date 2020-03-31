from os import system

system('title Pseudo Cálculadora')
op = 4
while op != 5:
    if op == 4:
        system('cls')
        valor1 = float(input('\n\tDigite o 1° valor: '))
        valor2 = float(input('\tDigite o 2° valor: '))
    system('cls')
    op = int(input("""
    \t   • Números Digitados:
    \t         ({}; {})
    \t +----------------------+
    \t |  PSEUDO CÁLCULADORA  |
    \t +----------------------+
    \t | [1] Soma             |
    \t | [2] Multiplicar      |
    \t | [3] Maior            |
    \t | [4] Novos Números    |
    \t | [5] Sair do Programa |
    \t +----------------------+
    
    \t  • Digite uma opção: """.format(valor1, valor2)))
    while (op != 1) and (op != 2) and (op != 3) and (op != 4) and (op != 5):
        print('\n\t  !!! OPÇÃO INVÁLIDA !!!\n')
        system('pause')
        system('cls')
        op = int(input("""
           • Números Digitados:
                 ({}; {})
         +----------------------+
         |  PSEUDO CÁLCULADORA  |
         +----------------------+
         | [1] Soma             |
         | [2] Multiplicar      |
         | [3] Maior            |
         | [4] Novos Números    |
         | [5] Sair do Programa |
         +----------------------+

          • Digite uma opção: """.format(valor1, valor2)))
    if op == 1:
        # Soma
        print('\n\tSoma dos números digitados:\n\t{} + {} = {}\n'.format(valor1, valor2, valor1 + valor2))
        system('pause')
    elif op == 2:
        # Multiplica
        print('\n\tMultiplicação dos números digitados:\n\t{} x {} = {}\n'.format(valor1, valor2, valor1 * valor2))
        system('pause')
    elif op == 3:
        # Maior
        print('\n\tMaior dos números digitados = {}\n'.format(valor1 if valor1 > valor2 else valor2))
        system('pause')
