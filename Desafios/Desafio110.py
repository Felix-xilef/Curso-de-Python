from auxiliar import receberInt, receberFixo
import moeda

# main
menu = f"""
\t {'=~'*20}=
\t :{'Digite uma Opção':^39}:
\t {'=~'*20}=
\t : {'[1] - Inserir valor':<37} :
\t : {'[2] - Encerrar':<37} :
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
        moeda.resumo(val=float(input(f'\n\tDigite o preço: {md}')), porcAum=float(input('\n\tDigite a porcentagem de aumento (10 para 10%, 5 para 5%, etc): ')), porcDim=float(input('\n\tDigite a porcentagem de diminuição (10 para 10%, 5 para 5%, etc): ')), fmt=resp, mod=md, dec=desc)
    elif op == 2:
        break
    else:
        print('\n\t\t!!! OPÇÃO INVÁLIDA !!!')
