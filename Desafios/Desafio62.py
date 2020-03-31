termo1 = float(input('\n\tDigite o 1° termo da PA (progressão aritmética): '))
razao = float(input('\tDigite a razão da PA: '))
print('\n\tOs 10 primeiros termos desta PA são:')
i = 0
qtd = 10
while qtd != 0:
    qtd += i
    while i < qtd:
        print('\t{}° = {}'.format(i + 1, termo1 + (razao * i)))
        i += 1
    qtd = int(input('\n\tDigite a quantos termos mais você deseja mostrar (0 para finalizar): '))

input('\n\nPressione <enter> para continuar')
