qtd = -1
soma = n = 0
while n != 999:
    soma += n
    qtd += 1
    n = int(input('\tDigite um número (999 para encerrar): '))
print('\n\tQuantidade de números digitados = {}\n\tSoma dos números digitados = {}'.format(qtd, soma))

input('\n\nPressione <enter> para continuar')
