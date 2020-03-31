from random import randint

def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(0, 99))


def somaPar(lista):
    print('Soma entre os valores ', end='')
    s = 0
    for i in lista:
        if i % 2 ==0:
            print(f'{i} ', end='')
            s += i
    
    print(f'= {s}')
    


# main
numeros = list()
sorteia(numeros)
print(numeros)
somaPar(numeros)
print(numeros)

input('\n\nPressione <enter> para continuar')
