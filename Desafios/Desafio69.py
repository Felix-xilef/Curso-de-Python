m = mais18 = fMenos20 = 0
while True:
    idade = int(input('\n\tDigite a idade (em anos) da pessoa: '))
    if idade > 18:
        mais18 += 1
    while True:
        sexo = input('\tDigite o sexo da pessoa (masculino / feminino): ').strip().lower()
        if sexo == 'masculino':
            m += 1
            break
        elif sexo == 'feminino':
            if idade < 20:
                fMenos20 += 1
            break
        else:
            print('\t!!! Opção Inválida !!!')
    resp = input('\tDeseja Continuar? (sim / não) >').strip().lower()
    if resp != 'sim':
        break
print(f'\n\tN° de...\n\t\t...pessoass com mais de 18 anos = {mais18}\n\t\t...homens = {m}\n\t\t...mulheres com menos de 20 anos = {fMenos20}')

input('\n\nPressione <enter> para continuar')
