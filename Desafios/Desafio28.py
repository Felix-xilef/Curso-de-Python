from os import system
from random import randint

numero = randint(0, 5)
tentativa = int(input('\n\tAdivinhe um número de 0 a 5: '))
if numero == tentativa:
    print('\n\tParabéns! Você Acertou!\n')
else:
    print('\n\tVocê Errou!\n\tNúmero sorteado: {}\n'.format(numero))

system('pause')
