# import os
from os import system

print('Digite')
n1 = int(input('1° valor: '))
n2 = int(input('2° valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('\nSoma: {}\nProduto: {}\nDivisão: {}\nDivisão Inteira: {}\nPotência: {}\n'.format(s, m, d, di, e), end = '\n') # end = '' - seta a
#                                                                                                                       finalização do print 
#                                                                                                                       (útil para n pular linha)

#:.xf - adiciona formatação ao print da variável: .xf - um float com x números depois da vírgula (igual C)

# nome = input('Digite seu nome: ')
# print('Prazer em te conhecer {:=^20}!'.format(nome)) # : - adiciona formatação ao print da variável
#                                                      # = - preenche com iguais os espaços vazios
#                                                      # ^ - alinha ao centro dos espaços
#                                                      # 20 - printa um total de 20 caracteres

# os.system('pause')
system('pause')
