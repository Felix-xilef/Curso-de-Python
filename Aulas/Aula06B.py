import os

n = input('Digite algo: ')
print('isnumeric() = {}'.format(n.isnumeric())) #isnumeric() - verifica se valor é int
print('isalpha() = {}'.format(n.isalpha()))     #isalpha() - verifica se valor é alfa (somente letras)
print('isalnum() = {}'.format(n.isalnum()))     #isalnum() - verifica se valor é alfanumérico (contém letras e/ou números)
print('isupper() = {}'.format(n.isupper()))     #isupper() - verifica se valor esta todo em maiúsculo

os.system('pause')
