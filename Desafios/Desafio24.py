from os import system

cidade = input('\n\tDigite o nome da cidade: ')
print('\tComeça com santo = {}\n'.format(cidade.strip().lower().startswith('santo')))

system('pause')
