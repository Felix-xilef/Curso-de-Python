import os

print('Digite\n')
dias = int(input('\tQuantidade de dias que o carro foi alugado: '))
km = float(input('\tQuantidade de kilometros (km) percorridos: '))
print('\nPreço a pagar = R$ {:.2f}\n'.format((dias * 60) + (km * 0.15)))

os.system('pause')
