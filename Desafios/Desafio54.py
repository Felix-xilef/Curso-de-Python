from datetime import datetime

maiores = 0
for i in range(1, 8):
    nascimento = int(input('\tDigite o ano de nascimento da {}° pessoa: '.format(i)))
    if (datetime.now().year - nascimento) >= 18:
        maiores += 1
print('\n\tNúmero de pessoas maiores de idade = {}\n\tNúmero de pessoas menores de idade = {}'.format(maiores, 7 -maiores))

input('\n\nPressione <enter> para continuar')
