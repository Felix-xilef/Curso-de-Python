from auxiliar import receberInt

def ficha(nome='<desconhecido>', gols=0):
    if nome == '':
        nome = '<desconhecido>'
    from math import ceil
    linha = f"{'=~'*(ceil(len(nome)/2) + 9)}="
    print(f"""
    {linha}
    : {f'Ficha do(a) {nome}':^{(len(linha) - 4)}} :
    {linha}
    : {f'Número de gols -> {gols}':<{(len(linha) - 4)}} :
    {linha}""")


# main
gols = input('Digite a quantidade de gols: ')
ficha(input('Digite o nome do jogador: '), int(gols) if gols.isnumeric() else 0)

input('\n\nPressione <enter> para continuar')
