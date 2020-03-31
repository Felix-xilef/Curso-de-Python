# import Aula22uteis # módulo
from uteis import numeros # pacote

# main
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'{num}! = {fat}')
print(f'2 * {num} = {numeros.dobro(num)}')

input('\n\nPressione <enter> para continuar')
