from os import system

casa = float(input('\n\tDigite o valor da casa: R$ '))
salario = float(input('\tDigite o salário do comprador: R$ '))
anos = float(input('\tDigite em quantos anos o valor será quitado: '))
prestacao = casa / (anos * 12)
if prestacao > (0.3 * salario):
    print('\n\tEmprestimo Negado!\n')
else:
    print('\n\tEmprestimo Permitido!\n')

system('pause')
