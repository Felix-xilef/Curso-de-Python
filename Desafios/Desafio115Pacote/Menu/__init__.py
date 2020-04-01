def color(font=''):
    """
        -> Fornece o código ANSI para a cor de texto desejada, não forneça entrada para a cor padrão
        :param font:nome da cor desejada opções - preto, vermelho, verde, amarelo, azul, magenta, cyan e cinza claro
        :return:código ANSI para texto na cor escolhida
    """
    font.lower()
    cor = '\033['
    if font == 'preto':
        cor += '30'
    elif font == 'vermelho':
        cor += '31'
    elif font == 'verde':
        cor += '32'
    elif font == 'amarelo':
        cor += '33'
    elif font == 'azul':
        cor += '34'
    elif font == 'magenta':
        cor += '35'
    elif font == 'cyan':
        cor += '36'
    elif font == 'cinza claro':
        cor += '37'
    cor += 'm'
    return cor


def cabecalho(msg=''):
    """
        -> Cria um 'cabeçalho' no seguinte formato:
                ===========
                    msg
                ===========
        :param msg:mensagem que será usada no cabeçalho do menu (padrão = '')
        :return:string cabeçalho criado
    """
    tam = 50
    if len(msg) > tam:
        tam = len(msg) + 8

    interface = f"\n\t{color('amarelo')}{'='*tam}\n\t{color('azul')}{msg:^{tam}}\n\t{color('amarelo')}{'='*tam}{color()}"
    return interface


def menu(msg='Menu', pos='Digite uma opção: ', *op):
    """
        -> Cria um 'menu' no seguinte formato:
                ===========
                    msg
                ===========
                 op1
                 ...
                 opn
                ===========
                  pos
        :param msg:mensagem que será usada no cabeçalho do menu (padrão = 'Menu')
        :param pos:mensagem que será usada no fim do menu (padrão = 'Digite uma opção: ')
        :param *op:opções que serão mostradas no menu
        :return:string do menu criada
    """
    tam = 50
    interface = cabecalho(msg=msg)
    if len(msg) > tam:
        tam = len(msg) + 8

    for i in op:
        interface += f"\n\t{color('azul')}{(op.index(i) + 1):^3}{color('amarelo')} - {color('azul')}{i:<{tam - 6}}"

    interface += f"\n\t{color('amarelo')}{'='*tam}{color('azul')}\n\t  {pos}{color('verde')}"
    return interface


def erro(msg='ERRO'):
    """
        -> Cria uma mensagem de erro
        :param msg:mensagem que será usada no erro (padrão = 'ERRO')
        :return:string da mensagem de erro criada criada
    """
    return f"\t{color('vermelho')}{msg}{color()}"
