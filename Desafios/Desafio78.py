numeros = list()
for i in range(0, 5):
    numeros.append(float(input('\tDigite um número: ')))
maior = max(numeros)
menor = min(numeros)
print(f'\n\tMaior valor digitado = {maior} - Posição: {numeros.index(maior) + 1}°\n\tMenor valor digitado = {menor} - Posição: {numeros.index(menor) + 1}°')

input('\n\nPressione <enter> para continuar')
