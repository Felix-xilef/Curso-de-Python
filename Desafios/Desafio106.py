def entreLinhas(msg):
    return f"{azul}{'~' * (len(msg) + 4)}\n{msg:^{len(msg) + 4}}\n{amarelo}{'~' * (len(msg) + 4)}{normal}"


# main
normal = '\033[m'
azul = '\033[34m'
amarelo = '\033[33m'
vermelho = '\033[31m'
while True:
    comando = input(f"{entreLinhas(f'Sistema de Ajuda {amarelo}PyHELP')}\n{vermelho}  Função ou biblioteca > {normal}").strip().lower()
    if comando == 'fim':
        break
    print(entreLinhas(f'Acessando o manual do comando {amarelo}{comando}'), end='\n\n')
    help(comando)

input(f'{vermelho}\n\nPressione <enter> para continuar{normal}')
