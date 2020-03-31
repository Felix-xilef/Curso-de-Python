from auxiliar import receberInt

valores = [[], []]
for i in range(0, 7):
    num = receberInt()
    valores[num % 2].append(num)

print(f'\n\tPares em ordem: {sorted(valores[0])}\n\tÍmpares em ordem: {sorted(valores[1])}')

input('\n\nPressione <enter> para continuar')
