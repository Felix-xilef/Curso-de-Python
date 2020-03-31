from os import system

nome = input('\n\tDigite seu nome: ').strip()
if nome.lower() == 'felix':
    print('\n\tQue nome lindo você tem!')
else:
    print('\n\tSeu nome é tão normal!')
print('\n\tBom dia, {}!\n'.format(nome))

system('pause')
