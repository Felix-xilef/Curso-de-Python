produtos = ('lápis', 1.75, 'borracha', 2, 'caderno', 15.9, 'estojo', 25, 'transferidor', 4.2, 'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.3, 'livro', 34.9)
print("""
\t +------------------------------------------+
\t |            Listagem de Preços            |
\t +------------------------------------------+""")
for i in range(0, len(produtos), 2):
    print(f'\t | {produtos[i].capitalize():.<31}R${produtos[i + 1]:>7.2f} |')
print('\t +------------------------------------------+')

input('\n\nPressione <enter> para continuar')
