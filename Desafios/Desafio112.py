from auxiliar import receberInt, receberFixo
from utilidadesCeV import moeda, dado

# main
menu = f"""
\t {'=~'*20}=
\t :{'Digite uma Opção':^39}:
\t {'=~'*20}=
\t : {'[1] - Inserir valor':<37} :
\t : {'[2] - Encerrar':<37} :
\t {'=~'*20}=
\t   > """

while True:
    op = receberInt(menu)
    if op == 1:
        moeda.resumo(val=dado.leiaDinheiro('\n\tDigite o preço: '), porcAum=float(input('\n\tDigite a porcentagem de aumento (10 para 10%, 5 para 5%, etc): ')), porcDim=float(input('\n\tDigite a porcentagem de diminuição (10 para 10%, 5 para 5%, etc): ')))
    elif op == 2:
        break
    else:
        print('\n\t\t!!! OPÇÃO INVÁLIDA !!!')
