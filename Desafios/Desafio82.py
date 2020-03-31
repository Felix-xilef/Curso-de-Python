from auxiliar import receberInt, receberSN

valores = list()
while True:
    valores.append(receberInt())
    resp = receberSN()
    if resp == 'n':
        break

pares = []
impares = list()
for i in valores:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'\n\tPares = {pares}\n\tÍmpares = {impares}')

input('\n\nPressione <enter> para continuar')
