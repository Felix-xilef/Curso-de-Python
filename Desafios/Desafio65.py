media = qtd = 0
resp = ''
while resp != 'não':
    n = int(input('\n\tDigite um número inteiro: '))
    if qtd == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    media += n
    qtd += 1
    resp = input('\tDeseja digitar outro? (sim / não) >').strip().lower()
    while resp != 'sim' and resp != 'não':
        resp = input('\t------------------------\n\t!!! RESPOSTA INVÁLIDA !!!\n\t------------------------\n\tDeseja digitar outro? (sim / não) >').strip().lower()
print('\n\tMédia dos valores digitados = {}\n\tMaior valor digitado = {}\n\tMenor valor digitado = {}'.format(media/qtd, maior, menor))

input('\n\nPressione <enter> para continuar')
