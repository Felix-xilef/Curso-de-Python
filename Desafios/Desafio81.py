numeros = []
while True:
    while True:
        resp = input('\n\tDigite um número inteiro: ').strip()
        if resp.isnumeric():
            numeros.append(int(resp))
            break
        else:
            print('\t!!! Resposta Inválida !!!')

    while True:
        resp = input('\tDeseja continuar? (S / N): ').strip().lower()
        if resp != 's' and resp != 'n':
            print('\t!!! Resposta Inválida !!!')
        else:
            break

    if resp == 'n':
        break

print(f'\n\tQuantidade de números digitados = {len(numeros)}\n\tValores ordenados de forma decrescente:\n\t{sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('\tO valor 5 está na lista')
else:
    print('\tO valor 5 não está na lista')

input('\n\nPressione <enter> para continuar')
