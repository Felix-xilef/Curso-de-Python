from os import system
from datetime import datetime

nascimento = int(input('\n\tDigite o ano de nascimento do atleta: '))
idade = datetime.now().year - nascimento
print('\n\tCategoria do atleta: ', end='')
if idade <= 9:
    print('Mirim\n')
elif idade <= 14:
    print('Infantil\n')
elif idade <= 19:
    print('Junior\n')
elif idade <= 20:
    print('Sênior\n')
else:
    print('Master\n')

system('pause')
