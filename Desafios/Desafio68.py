from os import system
from random import randint

system('title Jogo do Par ou Impar')
v = 0
while True:
    while True:
        system('cls')
        escolha = input(f"""
         =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
         :              Par ou Ímpar               :
         =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
         : Vitórias: {v:<30}:
         +-----------------------------------------+
           Digite sua escolha (par / ímpar): """).strip().lower()
        if escolha == 'par' or escolha == 'ímpar':
            break
        elif escolha == 'impar':
            escolha = 'ímpar'
            break
        print('\t   !!! OPÇÃO INVÁLIDA !!!\n')
        system('pause')
    numeroJ = int(input('\t   Digite o número escolhido: '))
    numeroC = randint(0, 100)
    if (numeroJ + numeroC) % 2 == 0:
        res = 'par'
    else:
        res = 'ímpar'
    print(f"""\t +-----------------------------------------+
    \t | Sua escolha: {escolha:<27}|
    \t | Seu número: {numeroJ:<28}|
    \t | Número do computador: {numeroC:<18}|
    \t | Resultado: {res:29}|
    \t =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
    if res == escolha:
        print("""\t :       PARABÉNS !!! VOCÊ GANHOU !!!      :
         =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n""")
        v += 1
        system('pause')
    else:
        print("""\t :              VOCÊ PERDEU !!!            :
         =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
        break
print(f'\t   Game Over! Você venceu {v} vezes\n')

system('pause')
# input('\n\nPressione <enter> para continuar')
