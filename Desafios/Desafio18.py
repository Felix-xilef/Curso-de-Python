from os import system
from math import sin, cos, tan, radians

a = float(input('\n\tDigite um ângulo em graus (°): '))
print('\n\tSen({0}) = {1}\n\tCos({0}) = {2}\n\tTg({0}) = {3}\n'.format(a, sin(radians(a)), cos(radians(a)), tan(radians(a))))

system('pause')
