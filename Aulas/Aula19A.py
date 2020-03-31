# Dicionários {} / dict() - como uma lista, porém o indice pode ser definido (key)
pessoas = {'nome': 'Felix', 'sexo': 'm', 'idade': 18}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())
for k, v in pessoas.items():
    print(k, '=', v)

del pessoas['sexo']
print(pessoas)
pessoas['nome'] = 'Gustavo'
print(pessoas)
pessoas['peso'] = 74
print(pessoas)

input('\n\nPressione <enter> para continuar')
