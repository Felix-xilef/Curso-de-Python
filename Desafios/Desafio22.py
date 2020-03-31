from os import system

nome = input('\n\tDigite um nome completo: ')
print("""\n\tNome com:
\n\tTodas as letras maiusculas: {}
\tTodas as letras minúsculas: {}
\n\tQuantidade de letras (sem espaços) = {}
\tQuantidade de letras do primeiro nome = {}\n""".format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), len(nome[:nome.find(' ')])))

system('pause')
