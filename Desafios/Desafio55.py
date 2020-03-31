for i in range(1, 6):
    peso = float(input('\tDigite o peso da {}° pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('\n\tMaior peso registrado = {}\n\tMenor peso registrado = {}'.format(maior, menor))        

input('\n\nPressione <enter> para continuar')
