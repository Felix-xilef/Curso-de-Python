media = 0
mulheresMenos20 = 0
for i in range(1, 5):
    nome = input('\n\tDigite as seguintes informações sobre a pessoa {}:\n\t\tNome: '.format(i)).strip()
    idade = int(input('\t\tIdade (anos): '))
    sexo = input('\t\tSexo (biológico) (masculino / feminino): ').strip().lower()
    media += idade
    if sexo == 'masculino' and i == 1:
        hmvNome = nome
        hmvIdade = idade
    elif sexo == 'masculino' and idade > hmvIdade:
        hmvNome = nome
        hmvIdade = idade
    elif sexo == 'feminino' and idade < 20:
        mulheresMenos20 += 1
media /= 4
print("""
\tMédia de idade do grupo = {}
\tHomem mais velho = {}
\tQuantidade de mulheres com menos de 20 anos = {}""".format(media, hmvNome, mulheresMenos20))

input('\n\nPressione <enter> para continuar')
