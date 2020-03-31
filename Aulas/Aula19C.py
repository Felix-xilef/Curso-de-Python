estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('\n\tUnidade Federativa: ').strip()
    estado['sigla'] = input('\tSigla: ').strip().upper()
    brasil.append(estado.copy()) # .copy() - retorna uma cópia do dicionário (não é possível fazer fatiamento em dicionário) - para não criar vínculo

for e in brasil:
    print('\n')
    for k, v in e.items():
        print(f'\t{k} - {v}')

input('\n\nPressione <enter> para continuar')
