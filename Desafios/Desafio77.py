palavras = 'lapis', 'borracha', 'caderno', 'estojo', 'transferidor', 'compasso', 'mochila', 'canetas', 'livro', 'caiu', 'k', 'h', 'l', 'a', 'c', 'o', 'w', 'f', 'g', 'm', 'chapecoense', 'ç', 'b', 's', 'z', 'x', 'n', 'v', 'q', 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
for i in palavras:
    print(f'\n\tNa palavra {i} temos', end='')
    for j in i:
        if 'a' in j.lower():
            print(' a', end='')
        if 'e' in j.lower():
            print(' e', end='')
        if 'i' in j.lower():
            print(' i', end='')
        if 'o' in j.lower():
            print(' o', end='')
        if 'u' in j.lower():
            print(' u', end='')

input('\n\nPressione <enter> para continuar')
