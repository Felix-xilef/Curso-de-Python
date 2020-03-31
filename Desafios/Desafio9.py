import os

n = int(input('Digite um número: '))
print('\n\t0 x {0} = {1}\n\t1 x {0} = {2}\n\t2 x {0} = {3}\n\t3 x {0} = {4}'.format(n, n*0, n*1, n*2, n*3), end = '')
print('\n\t4 x {0} = {1}\n\t5 x {0} = {2}\n\t6 x {0} = {3}\n\t7 x {0} = {4}'.format(n, n*4, n*5, n*6, n*7), end = '')
print('\n\t8 x {0} = {1}\n\t9 x {0} = {2}\n\t10 x {0} = {3}\n'.format(n, n*8, n*9, n*10))

os.system('pause')
