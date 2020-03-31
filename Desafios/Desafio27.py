from os import system

nome = input('\n\tDigite um nome completo: ').split()
print("""\n\tPrimeiro Nome = {}
\tÚltimo Nome = {}\n""".format(nome[0], nome[len(nome) - 1]))

system('pause')
