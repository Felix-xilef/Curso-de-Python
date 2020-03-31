valores = []
while True:

    while True:
        resp = input('\n\tDigite um número inteiro: ').strip()
        if resp.isnumeric():
            num = int(resp)
            break
        else:
            print('\t!!! Resposta Inválida !!!')

    if (num in valores) == False:
        valores.append(num)
    else:
        print('\tValor já adicionado')

    while True:
        resp = input('\tDeseja continuar? (S / N): ').strip().lower()
        if resp != 's' and resp != 'n':
            print('\t!!! Resposta Inválida !!!')
        else:
            break

    if resp == 'n':
        break

print(f'\n\tValores digitados em ordem crescente:\n\t{sorted(valores)}')

input('\n\nPressione <enter> para continuar')
