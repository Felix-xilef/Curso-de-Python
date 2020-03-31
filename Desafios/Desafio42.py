from os import system

reta1 = float(input('\n\tDigite o comprimento da 1° reta: '))
reta2 = float(input('\tDigite o comprimento da 2° reta: '))
reta3 = float(input('\tDigite o comprimento da 3° reta: '))
if reta1 >= (reta2 + reta3):
    print('\n\tNão pode ser um triângulo!\n')
elif reta2 >= (reta1 + reta3):
    print('\n\tNão pode ser um triângulo!\n')
elif reta3 >= (reta1 + reta2):
    print('\n\tNão pode ser um triângulo!\n')
else:
    print('\n\tPode ser um triângulo!')
    if reta1 == reta2 and reta2 == reta3:
        print('\n\tO triângulo será Equilátero!\n')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('\n\tO triângulo será Isósceles!\n')
    else:
        print('\n\tO triângulo será Escaleno!\n')

system('pause')
