from os import system

frase = 'Curso em Vídeo Python'

print(end='\t')

print(frase[3], end='\n\t')
print(frase[3:13], end='\n\t')
print(frase[:13], end='\n\t')
print(frase[13:], end='\n\t')
print(frase[1:15:2], end='\n\t')
print(frase[1::2], end='\n\t')
print(frase[::2], end='\n\n\t')

print(frase.count('o'), end='\n\t')
print(frase.count('O'), end='\n\t')
print(frase.upper().count('O'), end='\n\n\t')

print(len(frase), end='\n\t')
frase = '   Curso em Vídeo Python   '
print(len(frase), end='\n\t')
print(len(frase.strip()), end='\n\n\t')

frase = frase.strip()
print(frase.replace('Python', 'Android'), end='\n\t')
print(frase, end='\n\t')
frase = frase.replace('Python', 'Android')
print(frase, end='\n\n\t')

frase = frase.replace('Android', 'Python')
print('Curso' in frase, end='\n\t')
print(frase.find('Curso'), end='\n\t')
print(frase.find('Vídeo'), end='\n\t')
print(frase.find('vídeo'), end='\n\t')
print(frase.lower().find('vídeo'), end='\n\n\t')

print(frase.split(), end='\n\t')
dividido = frase.split()
print(dividido, end='\n\t')
print(dividido[0], end='\n\t')
print(dividido[2], end='\n\t')
print(dividido[2][3], end='\n\n')

print("""Welcome! Are you completely new to programming?
about why and how to get started with Pyton. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
It's also easy for beginners to use and learn, so jump in!\n""")

system('pause')
