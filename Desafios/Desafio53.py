frase = input('\n\tDigite uma frase: ').strip().lower().replace(' ', '').replace(',', '').replace('.', '').replace('-', '')
tamanho = len(frase) - 1
for i in range(0, int(tamanho/2) + 1):
    if frase[i] != frase[tamanho - i]:
        print('\n\tEssa frase não é um palíndromo!')
        input('\n\nPressione <enter> para continuar')
        exit()
print('\n\tEssa frase é um palíndromo!')

input('\n\nPressione <enter> para continuar')
