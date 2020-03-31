from auxiliar import receberInt
from random import randint

jogos = list()
jogoIndividual = list()
qtd = receberInt('\tDigite a quantidade de jogos a serem efetuados: ')
for i in range(0, qtd):
    for j in range(0, 6):
        while True:
            aux = randint(1, 60)
            if aux not in jogoIndividual:
                jogoIndividual.append(aux)
                break
    
    jogoIndividual.sort()
    jogos.append(jogoIndividual[:])
    jogoIndividual.clear()

for i in jogos:
    print(f'\n\t{jogos.index(i) + 1:>3}° jogo -> {i}', end='')

input('\n\nPressione <enter> para continuar')
