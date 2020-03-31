from os import system
from random import randint

system('title Jokenpô')
jogador = int(input("""
\t --------------------------
\t |         JOKENPÔ        |
\t --------------------------
\t | [1] Pedra              |
\t | [2] Papel              |
\t | [3] Tesoura            |
\t --------------------------
\t  Digite a sua escolha: """))
maquina = randint(1, 3)
if (jogador != 1) and (jogador != 2) and (jogador != 3):
    print('\n\t  Opção Inválida!\n')
    system('pause')
    exit()
elif jogador == maquina:
    print('\n\t  EMPATE!')
elif (jogador > maquina) or (jogador == 1 and maquina == 3):
    print('\n\t  VITÓRIA!')
else:
    print('\n\t  DERROTA!')
print('\n\t  Sua escolha: {}\n\t  Escolha do computador: {}\n'.format(jogador, maquina).replace('1', 'Pedra').replace('2', 'Papel').replace('3', 'Tesoura'))

system('pause')
