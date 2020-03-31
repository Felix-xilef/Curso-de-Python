from os import system

ano = int(input('\n\tDigite um ano: '))
print('\n\t{} '.format(ano), end='')
if (ano % 4) != 0:
    print('não ', end='')
elif (ano % 100) == 0:
    if (ano % 400) != 0:
        print('não ', end='')
print('é bissexto!\n')

system('pause')
