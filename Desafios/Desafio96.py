from auxiliar import receberSN

def area():
    l = float(input('\nDigite a largura do terreno: '))
    c = float(input('Digite o comprimento do terreno: '))
    print(f'\nA área do terreno vale {l*c}')


# main
while True:
    area()
    resp = receberSN()
    if resp == 'n':
        break

input('\n\nPressione <enter> para continuar')
