import os

print('Digite em metros(m):\n')
h = float(input('\tA altura da parede: '))
l = float(input('\tA largura da parede: '))
print('\nÁrea da prede = {} m2\nTinta necessária para pintar a parede: {} L'.format(l*h, (l*h)/2))

os.system('pause')