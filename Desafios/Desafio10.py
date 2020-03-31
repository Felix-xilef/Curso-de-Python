import os

n = float(input('Digite o valor que você tem na carteira (R$): '))
print('\nVocê pode comprar US${:.2f}\n'.format(n/3.27))

os.system('pause')