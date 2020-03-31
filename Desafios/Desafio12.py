import os

p = float(input('Digite o preço do produto (R$): '))
print('\nNovo preço com 5% de desconto = R$ {:.2f}\n'.format(p*0.95))

os.system('pause')