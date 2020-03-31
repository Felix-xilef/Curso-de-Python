from os import system

peso = float(input('\n\tDigite seu peso (kg): '))
altura = float(input('\tDigite sua altura (m): '))
imc = peso/(altura**2)
print('\n\tIMC = {}'.format(imc))
if imc < 18.5:
    print('\t!! Abaixo do peso ideal !!\n')
elif imc < 25:
    print('\tPeso Ideal!\n')
elif imc < 30:
    print('\t! Sobrepeso !\n')
elif imc < 40:
    print('\t!! Obesidade !!\n')
else:
    print('\t!!! Obesidade Mórbida !!!\n')

system('pause')
