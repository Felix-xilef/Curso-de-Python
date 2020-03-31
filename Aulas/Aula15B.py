nome = 'José'
idade = 33

print(f'\n\tO {nome} tem {idade} anos') # Python 3.6+
print('\n\tO {} tem {} anos'.format(nome, idade)) # Python 3
print('\n\tO %s tem %d anos' % (nome, idade)) # Python 2

salario = 987.3
print(f'\n\tO {nome:-^20} tem {idade} anos e ganha R${salario:.2f}')

input('\n\nPressione <enter> para continuar')
