from os import system

km = float(input('\n\tDigite a distância da viagem em kilometros (km): '))
print('\n\tPreço da passagem = R$ ', end='')
if km <= 200:
    print('{:.2f}\n'.format(km * 0.5))
else:
    print('{:.2f}\n'.format(km * 0.45))

system('pause')
