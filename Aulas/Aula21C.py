def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


# main
num = int(input('Digite um número para descobrir se é par ou ímpar: '))
print(f'{num} é ', end='')
print('par' if par(num) else 'ímpar')

input('\n\nPressione <enter> para continuar')
