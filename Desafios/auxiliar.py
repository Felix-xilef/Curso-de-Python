def receberInt(msg = '\tDigite um número inteiro: '):
    """
        -> Valida a entrada de um número inteiro pelo teclado*Caso a entrada seja inválida será exigidauma nova entrada.
        :param msg:mensagem a ser impressa
        :return:número inteiro recebido
    """
    while True:
        resp = input(msg).strip()
        if resp.isnumeric():
            num = int(resp)
            break
        else:
            print('\t!!! Resposta Inválida !!!')
    return num


def receberFixo(msg, opcoes):
    """
        -> Valida a entrada de uma string pelo teclado*Caso a entrada seja inválida será exigidauma nova entrada.
        :param msg:mensagem a ser impressa
        :param opcoes:opções para a validação da entrada (todas opções em uma única string, sendo que caso tenha mais uma opção de validação cada uma dever ser de um único caracter)
        :return:string recebida
    """
    while True:
        resp = input(msg).strip().lower()
        if resp not in opcoes:
            print('\t!!! Resposta Inválida !!!')
        else:
            break
    return resp

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
