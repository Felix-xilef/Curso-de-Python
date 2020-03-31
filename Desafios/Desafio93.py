from auxiliar import receberInt

jogador = dict()
jogador['nome'] = input('\n\tDigite o nome do jogador: ')
qtdPartidas = receberInt('\tDigite o número de partidas jogadas: ')
aproveitamento = list()
totalGols = 0
for i in range(0, qtdPartidas):
    aproveitamento.append(receberInt(f'\t\tDigite a quantidade de gols da {i + 1}°: '))
    totalGols += aproveitamento[i]

jogador['aproveitamento'] = aproveitamento[:]
jogador['total de gols'] = totalGols
print(jogador)


input('\n\nPressione <enter> para continuar')
