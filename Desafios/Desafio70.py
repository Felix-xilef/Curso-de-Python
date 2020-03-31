total = qtd = precoBarato = 0
nomeBarato = ''
while True:
    nome = input('\n\tDigite o nome do produto: ').strip()
    preco = float(input('\tDigite o preço do produto: R$ '))
    total += preco
    if preco > 1000:
        qtd += 1
    if precoBarato > preco or total == preco:
        nomeBarato = nome
        precoBarato = preco
    while True:
        resp = input('\tDeseja continuar? (sim / não) >')
        if resp != 'sim' and resp != 'não':
            print('\t!!! Opção Inválida !!!')
        else:
            break
    if resp == 'não':
        break
print(f'\n\tTotal gasto = R$ {total}\n\tQuantidade de produtos que custam mais de R$1000,00 = {qtd}\n\tProduto mais barato = {nomeBarato}')

input('\n\nPressione <enter> para continuar')
