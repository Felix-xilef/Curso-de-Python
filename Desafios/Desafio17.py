from os import system
from math import sqrt

print('Digite a medida do:\n')
c1 = float(input('\t1° Cateto: '))
c2 = float(input('\t2° Cateto: '))
print('\n\tA hipotenusa do triângulo vale {}\n'.format(sqrt((c1**2) + (c2**2))))

system('pause')
