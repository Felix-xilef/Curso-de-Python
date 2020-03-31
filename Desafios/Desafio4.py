import os

algo = input('Digite algo: ')
print('O que você digitou é do tipo {}\ne é:'.format(type(algo)))
print('Alfanumérico: {}\nAlfabetico (Alfa): {}\nDecimal: {}\nNumérico: {}\nTodo Minúsculo: {}\nTodo Maiúsculo: {}\nUm Espaço: {}\n'.format(algo.isalnum(), algo.isalpha(), algo.isdecimal(), algo.isnumeric(), algo.islower(), algo.isupper(), algo.isspace()))


os.system('pause')
