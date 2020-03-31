cont = soma = 0
while True:
    n = int(input('\tDigite um número inteiro (999 para encerrar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"""
\t +-----------------------------------+
\t | Informações dos Valores Digitados |
\t +-----------------------------------+
\t | Quantidade = {cont:<21}|
\t | Soma = {soma:<27}|
\t +-----------------------------------+""")

input('\n\nPressione <enter> para continuar')
