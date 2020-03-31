teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
galera.append(teste[:]) # appende é como igualar (tem que salvar uma cópia - [:], se não cria-se um vínculo)
print(galera)

teste[0] = 'Felix'
teste[1] = 18
galera.append(teste[:])
print(galera)

input('\n\nPressione <enter> para continuar')
