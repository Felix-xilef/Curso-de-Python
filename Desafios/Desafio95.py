from auxiliar import receberInt, receberFixo

jogadores = list() # [dict(jogador), dict(jogador), ...]
jogador = dict() # {'nome': nome, 'total de gols': total, 'aproveitamento': list(aproveitamento)}
aproveitamento = list() # [int, int, int, ...]
while True:
    jogador['nome'] = input('\n\tDigite o nome do jogador: ')
    qtdPartidas = receberInt('\tDigite o número de partidas jogadas: ')
    jogador['total de gols'] = 0
    for i in range(0, qtdPartidas):
        aproveitamento.append(receberInt(f'\t\tDigite a quantidade de gols da {i + 1}°: '))
        jogador['total de gols'] += aproveitamento[i]

    jogador['aproveitamento'] = aproveitamento[:]
    aproveitamento.clear()
    jogadores.append(jogador.copy())
    if receberFixo('Deseja continuar? (s / n): ', 'sn') == 'n':
        break

while True:
    print('\n\t +-ID-+-Nome-----------------+-Gols------------+-Total-+')
    aux = 0
    for i in jogadores:
        aux = jogadores.index(i)
        print(f"\t + {aux:<2} + {i['nome']:<20} + {str(i['aproveitamento']):<15} + {i['total de gols']:^5} +")
    print(f"\t + {aux+1:<2} + Encerrar{' '*13}+{' '*17}+{' '*7}+")
    print(f"\t +{'-'*4}+{'-'*22}+{'-'*17}+{'-'*7}+")
    
    resp = receberInt(f'\n\t   Digite o ID do jogador para mostrar seus dados: ')

    if resp == aux+1:
        break
    elif resp < len(jogadores):
        print(f"\n\t +-Levantamento-do(a)-{jogadores[resp]['nome']:-^20}-+")
        for indexI, i in enumerate(jogadores[resp]['aproveitamento']):
            print(f"\t   • No {indexI}° jogo fez {i} gols")
        print(f"\t  Total de gols = {jogadores[resp]['total de gols']}")
    else:
        print(f'\n\t {"!!! Opção Inválida !!!":^45}')

input('\n\nPressione <enter> para continuar')
