from os import system
from random import shuffle

print('Digite o nome do:\n')
a1 = input('\t1° aluno: ')
a2 = input('\t2° aluno: ')
a3 = input('\t3° aluno: ')
a4 = input('\t4° aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista) #shuffle(nomedalista) - embaralha elementos da lista
print('A ordem de apressentação será:\n')
print(lista, end='\n\n')

system('pause')
