from auxiliar import receberInt, receberFixo

pessoaIndividual = dict()
pessoas = list()
mediaIdade = 0
while True:
    pessoaIndividual['nome'] = input('\n\tDigite o nome: ').strip().capitalize()
    pessoaIndividual['sexo'] = receberFixo('\tDigite o sexo (m / f): ', 'mf')
    pessoaIndividual['idade'] = receberInt('\tDigite a idade (anos): ')
    mediaIdade += pessoaIndividual['idade']
    pessoas.append(pessoaIndividual.copy())
    resp = receberFixo('\tDeseja continuar? (s / n): ', 'sn')
    if resp == 'n':
        break

mediaIdade = mediaIdade / len(pessoas)
mulheres = list()
idadeAcMd = list()
for i in pessoas:
    if i['sexo'] == 'f':
        mulheres.append(i.copy())
    if i['idade'] > mediaIdade:
        idadeAcMd.append(i.copy())

print(f'\n\tTotal de pessoas cadastradas = {len(pessoas)}\n\tMédia de idade do grupo = {mediaIdade}\n\tMulheres = {mulheres}\n\tPessoas com idade acima da média = {idadeAcMd}')

input('\n\nPressione <enter> para continuar')
