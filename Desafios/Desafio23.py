from os import system

# COM STRING:
numero = input('\n\tDigite um número de 0 a 9999: ').strip()
numero = numero.zfill(4)
print("""\n\tUnidade: {}
\tDezena: {}
\tCentena: {}
\tMilhar: {}\n""".format(numero[3], numero[2], numero[1], numero[0]))

# MATEMÁTICAMENTE:
numero = int(input('\n\tDigite um número de 0 a 9999: '))
print("""\n\tUnidade: {}
\tDezena: {}
\tCentena: {}
\tMilhar: {}\n""".format(numero % 10, int((numero / 10) % 10), int((numero / 100) % 10), int((numero / 1000) % 10)))

system('pause')
