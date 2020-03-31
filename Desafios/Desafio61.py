termo1 = float(input('\n\tDigite o 1° termo da PA (progressão aritmética): '))
razao = float(input('\tDigite a razão da PA: '))
print('\n\tOs 10 primeiros termos desta PA são:')
i = 0
while i < 10:
    print('\t{}° = {}'.format(i + 1, termo1 + (razao * i)))
    i += 1

input('\n\nPressione <enter> para continuar')
