import os

s = float(input('Digite o salário do funcionário (R$): '))
print('\nNovo salário com 15% de aumento = R$ {:.2f}\n'.format(s * 1.15))

os.system('pause')