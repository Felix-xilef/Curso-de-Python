from os import system

frase = input('\n\tDigite uma frase: ').lower().strip()
print("""\n\tQuantidade de vezes que aparece a letra 'a': {}
\tPosição da primeira letra 'a': {}
\tPosição da ultima letra 'a': {}\n""".format(frase.count('a'), frase.find('a'), frase.rfind('a')))

system('pause')
