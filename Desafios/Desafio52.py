numero = int(input('\n\tDigite um número inteiro: '))
for i in range(2, numero):
    if numero % i == 0:
        print('\n\tO Número não é primo!')
        input('\n\nPressione <enter> para continuar')
        exit()
print('\n\tO número é primo!')

input('\n\nPressione <enter> para continuar')
