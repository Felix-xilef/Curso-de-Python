from os import system
from random import choice

print('Digite o nome do:\n')
a1 = input('\t1° aluno: ')
a2 = input('\t2° aluno: ')
a3 = input('\t3° aluno: ')
a4 = input('\t4° aluno: ')
lista = [a1, a2, a3, a4] # criação de lista: nomedalista = [elemento1, elemento2, ..., elementon]
print('\n\t{} apagará a lousa\n'.format(choice(lista))) # choice(nomedalista) - escolhe um elemeto da lista

system('pause')
