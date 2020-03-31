from random import randint
from os import system

system('title Jogo da Adivinhação')
vezes = 0
jogador = int(input("""
\t   • Número da tentativa
\t  atual: {}°

\t +---------------------------+
\t |    JOGO DA ADIVINHAÇÃO    |
\t +---------------------------+
\t | Regras:                   |
\t |    Tente adivinhar o      |
\t | número de 0 a 10 sorteado |
\t | pelo computador           |
\t +---------------------------+

\t  • Digite seu palpite: """.format(vezes + 1)))
vezes += 1
computador = randint(0, 11)
while jogador != computador:
    print('\n\tERROU!\n\tTente novamente\n')
    system('pause')
    system('cls')
    jogador = int(input("""
    \t   • Número da tentativa
    \t  atual: {}°

    \t +---------------------------+
    \t |    JOGO DA ADIVINHAÇÃO    |
    \t +---------------------------+
    \t | Regras:                   |
    \t |    Tente adivinhar o      |
    \t | número de 0 a 10 sorteado |
    \t | pelo computador           |
    \t +---------------------------+

    \t  • Digite seu palpite: """.format(vezes + 1)))
    vezes += 1
print('\n\t!!! ACERTOU !!!\n\tParabéns! Você acertou em {} tentativas\n'.format(vezes))

system('pause')
# input('\n\nPressione <enter> para continuar') -> como tive que importar system, compensa usar o pause
