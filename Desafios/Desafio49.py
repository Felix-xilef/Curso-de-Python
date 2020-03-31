n = int(input('\n\tDigite um número: '))
print('\n\tTabuádo do {}:'.format(n))
for i in range(0, 11):
    print('\t {} x {} = {}'.format(n, i, n*i))

input('\n\nPressione <enter> para continuar')
