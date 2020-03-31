# for i in range(1, 5):
#     n = int(input('\tDigite um valor: '))
# print('\n\tFIM')

# n = -1
# while n != 0:
#     n = int(input('\tDigite um valor (0 para finalizar): '))
# print('\n\tFIM')

resp = 'sim'
while resp == 'sim':
    n = int(input('\n\tDigite um valor: '))
    resp = input('\tDeseja continuar? (sim / não) >').strip().lower()
print('\n\tFIM')

input('\n\nPressione <enter> para continuar')
