from os import system

num = int(input('\n\tDigite um número inteiro: '))
if (num % 2) == 0:
    print('\n\t{} é par!\n'.format(num))
else:
    print('\n\t{} é ímpar!\n'.format(num))

system('pause')
