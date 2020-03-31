numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    num = input('\n\tDigite um número de 0 a 20: ')
    if num.isnumeric() and int(num) >= 0 and int(num) <= 20:
        print(f'\tNúmero por extenço: {numeros[int(num)].capitalize()}')
        break
    else:
        print('\t!!! Valor Inválido !!!')

input('\n\nPressione <enter> para continuar')
