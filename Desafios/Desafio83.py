abreP = []
fechaP = list()
for i in input('\n\tDigite uma expressão matemática: '):
    if i == '(':
        abreP.append(i)
    elif i == ')':
        fechaP.append(i)

if len(abreP) == len(fechaP):
    print('\n\tSua expressão é válida!')
else:
    print('\n\tSua expressão não é válida!')

input('\n\nPressione <enter> para continuar')
