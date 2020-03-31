from auxiliar import receberInt, receberFixo

def fatorial(n, show=True):
    f = 1
    if show:
        print(n, end='! = ')
        for i in range(n, 1, -1):
            print(i, end=' * ')
            f *= i
        print(f'1 = {f}')
    else:
        for i in range(n, 0, -1):
            f *= i
    return f


# main
num = receberInt('Digite um número para descobrir seu fatorial: ')
resp = receberFixo('Mostrar processo de fatorial? (S / N): ', 'sn')
if resp == 's':
    fatorial(num)
else:
    print(f'{num}! = {fatorial(num, False)}')

input('\n\nPressione <enter> para continuar')
