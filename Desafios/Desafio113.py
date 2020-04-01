def leiaInt(msg='\tDigite um número inteiro: '):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print(f'{vermelho}O usuário preferiu não digitar um número inteiro{normal}')
            return 0
        except:
            print(f'{vermelho}ERRO: por favor, digite um número inteiro válido{normal}')
        else:
            return num


def leiaFloat(msg='\tDigite um número real: '):
    while True:
        try:
            num = float(input(msg))
        except KeyboardInterrupt:
            print(f'{vermelho}O usuário preferiu não digitar um número real{normal}')
            return 0.0
        except:
            print(f'{vermelho}ERRO: por favor, digite um número real válido{normal}')
        else:
            return num


# main

normal = '\033[m'
vermelho = '\033[31m'

while True:
    nInt = leiaInt()
    nFloat = leiaFloat()
    print(f'\n\t\tInt  =  {nInt}\n\t\tFloat = {nFloat}\n\n')

input('\n\nPressione <enter> para continuar')
