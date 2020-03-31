from os import system

tempo = int(input('\n\tQuantos anos tem seu carro?\n\t> '))

print('\n\n\t\t- Carro Novo -' if tempo <= 3 else '\n\n\t\t- Carro Velho -')

# if tempo <= 3:
#     print('\n\n\t\t- Carro Novo -')
# else:
#     print('\n\n\t\t- Carro Velho -')

print('\n\n\t---------------FIM---------------\n')

system('pause')
