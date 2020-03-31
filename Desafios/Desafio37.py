from os import system

numero = int(input('\n\tDigite o número inteiro na base 10 a ser convertido: '))
opcao = int(input("""
\t -------- CONVERSÕES --------
\t | [1] binário              |
\t | [2] octal                |
\t | [3] hexadecimal          |
\t ----------------------------
\t Digite a opção desejada: """))
if opcao == 1:
    print('\n\t{} na base 10 = {} na base 2\n'.format(numero, bin(numero).replace('0b', '')))
elif opcao == 2:
    print('\n\t{} na base 10 = {} na base 8\n'.format(numero, oct(numero).replace('0o', '')))
elif opcao == 3:
    print('\n\t{} na base 10 = {} na base 16\n'.format(numero, hex(numero).replace('0x', '').upper()))
else:
    print('\n\tOPÇÃO INVÁLIDA!\n')

system('pause')
