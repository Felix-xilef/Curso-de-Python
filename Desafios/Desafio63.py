n = int(input('\n\tDigite a quantidade de termos da Sequência de\n\tFibonacci você deseja mostrar: '))
print('\n\t',end='')
for i in range(0, n):
    print('~~~~~',end='')
print('~~~\n\t0 -> 1 -> ',end='')
i = 2
n0 = 0
n1 = 1
while i < n:
    n2 = n0 + n1
    print('{} -> '.format(n2),end='')
    n0 = n1
    n1 = n2
    i += 1
print('Fim\n\t',end='')
for i in range(0, n):
    print('~~~~~',end='')
print('~~~')

input('\n\nPressione <enter> para continuar')
