from os import system
# import math
from math import sqrt, floor

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

system('pause')
