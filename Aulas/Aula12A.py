from os import system

nome = input('\n\tDigite seu nome: ').strip().split()[0].capitalize()
if nome == 'Felix':
    print('\n\tQue nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('\n\tSeu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('\n\tBelo nome feminino')
else:
    print('\n\tSeu nome é bem normal!')
print('\n\tTenha um bom dia {}\n'.format(nome))

system('pause')
