from auxiliar import receberInt
from time import sleep

def contador(inicio, fim, passo):
    print('-'*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        passo *= -1
        fim -= 1
    else:
        fim += 1
    for i in range(inicio, fim, passo):
        sleep(0.5)
        print(f'{i} -> ', end='')
    print('FIM')
    print('-'*30)


# main
contador(1, 10, 1)
contador(10, 0, 2)
contador(receberInt('Digite o inicio: '), receberInt('Digite o fim: '), receberInt('Digite o passo: '))

input('\n\nPressione <enter> para continuar')
