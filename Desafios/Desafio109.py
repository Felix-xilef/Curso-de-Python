from auxiliar import receberInt, receberFixo
import moeda

def receberPreco():
    preco = float(input(f'\n\tDigite o preço: {md}'))
    return preco


def receberPorcentagem():
    preco = float(input('\n\tDigite a porcentagem (10 para 10%, 5 para 5%, etc): '))
    return preco


# main
menu = f"""
\t {'=~'*20}=
\t :{'Digite uma Opção':^39}:
\t {'=~'*20}=
\t : {'[1] - Aumentar o preço':<37} :
\t : {'[2] - Diminuir o preço':<37} :
\t : {'[3] - Dobrar o preço':<37} :
\t : {'[4] - Dividir o preço pela metade':<37} :
\t : {'[5] - Encerrar':<37} :
\t {'=~'*20}=
\t   > """

resp = receberFixo('\tDeseja receber os valores formatados em moeda? (s / n): ', 'sn')
if resp == 's':
    resp = True
    md = str(input('\tDigite a moeda em que deseja trabalhar (R$ para reais, US$ para dólar estadunidense, etc): '))
    desc = receberInt('\tDigite com quantas casas decimais você deseja trabalhar: ')
else:
    resp = False
    md = desc = ''

while True:
    op = receberInt(menu)
    if op == 1:
        porc = receberPorcentagem()
        pFinal = moeda.aumentar(receberPreco(), porc, fmt=resp, mod=md, dec=desc)
        print(f'\n\tPreço após o aumento de {porc}% = {pFinal}')
    elif op == 2:
        porc = receberPorcentagem()
        pFinal = moeda.diminuir(receberPreco(), porc, fmt=resp, mod=md, dec=desc)
        print(f'\n\tPreço após a diminuição de {porc}% = {pFinal}')
    elif op == 3:
        pFinal = moeda.dobro(receberPreco(), fmt=resp, mod=md, dec=desc)
        print(f'\n\tPreço dobrado = {pFinal}')
    elif op == 4:
        pFinal = moeda.metade(receberPreco(), fmt=resp, mod=md, dec=desc)
        print(f'\n\tPreço dividido pela metade = {pFinal}')
    elif op == 5:
        break
    else:
        print('\n\t\t!!! OPÇÃO INVÁLIDA !!!')
