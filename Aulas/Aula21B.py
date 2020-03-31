def fatorial(n=1):
    fat = 1
    for i in range(n, 1, -1):
        fat *= i
    return fat


# main
num = int(input('\n\tDigite um número para descobrir seu fatorial: '))
print(f'\n\t{num}! = {fatorial(num)}')
print(fatorial())

input('\n\nPressione <enter> para continuar')
