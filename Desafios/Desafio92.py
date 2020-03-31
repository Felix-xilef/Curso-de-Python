from auxiliar import receberInt
from datetime import datetime

pessoa = dict()
pessoa['nome'] = input('\n\tDigite seu nome: ').strip().capitalize()
anoAtual = int(datetime.now().year)
pessoa['idade'] = anoAtual - receberInt('\tDigite o ano de nascimento: ')
aux = receberInt('\tDigite a Carteira de Trabalho (0 - não tem): ')
if aux != 0:
    pessoa['ctps'] = aux
    aux = receberInt('\tDigite o ano de contratação: ')
    pessoa['contratação'] = aux
    pessoa['aposentadoria'] = (35 - (anoAtual - aux)) + pessoa['idade']
    pessoa['salário'] = float(input('\tDigite o salário: R$ '))

print(pessoa)

input('\n\nPressione <enter> para continuar')
