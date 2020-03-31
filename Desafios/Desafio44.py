from os import system

preco = float(input('\n\tDigite o preço normal do produto: '))
pagamento = int(input("""
\t -----------------------------------------
\t |         OPÇÕES DE PAGAMENTO           |
\t -----------------------------------------
\t | [1] À vista em dinheiro/cheque        |
\t | [2] À vista no cartão                 |
\t | [3] Em até 2x no cartão               |
\t | [4] Em 3x ou mais no cartão           |
\t -----------------------------------------
\t Digite a opção de pagamento desejada: """))
if pagamento == 1:
    print('\n\t Valor a ser pago: R$ {:.2f}\n'.format(0.9 * preco))
elif pagamento == 2:
    print('\n\t Valor a ser pago: R$ {:.2f}\n'.format(0.95 * preco))
elif pagamento == 3:
    print('\n\t Valor a ser pago: R$ {:.2f}\n'.format(preco))
elif pagamento == 4:
    print('\n\t Valor a ser pago: R$ {:.2f}\n'.format(1.2 * preco))
else:
    print('\n\tOpção Inválida!\n')

system('pause')
