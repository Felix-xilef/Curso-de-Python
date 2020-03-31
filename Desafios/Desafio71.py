valor = int(input("""
\t ================================================
\t |               Caixa Eletrônico               |
\t ================================================
\t   Digite o valor que você deseja sacar:
\t   R$ """))
print("""\t ================================================
\t | Quantidade de cédulas a ser(em) retirada(s): |""")
for i in [50, 20, 10, 1]:
    aux = valor // i
    if aux != 0:
        print(f'\t | R$ {i:<3}-> {aux:<36}|')
        valor = valor % i
print('\t ================================================')

input('\n\nPressione <enter> para continuar')
