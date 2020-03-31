from os import system

n1 = float(input('\n\tDigite a 1° nota: '))
n2 = float(input('\tDigite a 2° nota: '))
m = (n1 + n2)/2
print('\n\tA sua média foi {:.2f}'.format(m))

if m >= 6:
    print('\tSua média foi boa! PARABÉNS!\n')
else:
    print('\tSua média foi ruim! ESTUDE MAIS!\n')

print('\tPARABÉNS!\n' if m >= 6 else '\tESTUDE MAIS!\n')

system('pause')
