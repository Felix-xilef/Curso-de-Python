from os import system

salario = float(input('\n\tDigite o valor do salário: '))
print('\n\tValor do aumento = R$ ', end='')
if salario > 1250:
    print('{:.2f}\n'.format(salario * 0.1))
else:
    print('{:.2f}\n'.format(salario * 0.15))

system('pause')
