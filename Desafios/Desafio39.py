from os import system
from datetime import datetime

nascimento = int(input('\n\tDigite seu ano de nascimento (yyyy): '))
idade = datetime.now().year - nascimento
if idade < 18:
    print('\n\tVocê ainda vai se alistar!\n\tTempo até o alistamento: {} anos\n'.format(18 - idade))
elif idade == 18:
    print('\n\tAgora é a hora de você se alistar!\n')
else:
    print('\n\tJá passou do tempo de você se alistar!\n\tTempo desde o alistamento: {} anos\n'.format(idade - 18))

system('pause')
