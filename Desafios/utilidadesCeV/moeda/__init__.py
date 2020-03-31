def moeda(val, mod='R$', dec=2):
    """
        -> Formata o valor em moeda (R$XXXX,XX; US$XXXX,XX; etc)
        :param val:valor a ser formatado
        :param moeda:moeda para qual o valor será formatado (padrão = R$)
        :param dec:número de casas decimais a serem mostradas (padrão = 2)
        :return:retorna o valor formatado
    """
    return f'{mod}{val:.{dec}f}'


def aumentar(val, porc, fmt=True, mod='R$', dec=2):
    """
        -> Aumenta um valor em certa porcentagem
        :param val:valor a ser aumentado
        :param porc:porcentagem de quanto o valor deve ser aumentado (13 para 13%, 10 para 10%, etc)
        :param fmt:indica se o valor será formatado para moeda ou não (padrão = True)
        :param moeda:moeda para qual o valor será formatado (padrão = R$)
        :param dec:número de casas decimais a serem mostradas (padrão = 2)
        :return:retorna o valor aumentado
    """
    val *= ((100 + porc)/100)
    if fmt:
        return moeda(val=val, mod=mod, dec=dec)
    return val


def diminuir(val, porc, fmt=True, mod='R$', dec=2):
    """
        -> Diminui um valor em certa porcentagem
        :param val:valor a ser diminuido
        :param porc:porcentagem de quanto o valor deve ser diminuido (13 para 13%, 10 para 10%, etc)
        :param fmt:indica se o valor será formatado para moeda ou não (padrão = True)
        :param moeda:moeda para qual o valor será formatado (padrão = R$)
        :param dec:número de casas decimais a serem mostradas (padrão = 2)
        :return:retorna o valor com a diminuido
    """
    val *= ((100 - porc)/100)
    if fmt:
        return moeda(val=val, mod=mod, dec=dec)
    return val


def dobro(val, fmt=True, mod='R$', dec=2):
    """
        -> Dobra um valor
        :param val:valor a ser dobrado
        :param fmt:indica se o valor será formatado para moeda ou não (padrão = True)
        :param moeda:moeda para qual o valor será formatado (padrão = R$)
        :param dec:número de casas decimais a serem mostradas (padrão = 2)
        :return:retorna o valor dobrado
    """
    val *= 2
    if fmt:
        return moeda(val=val, mod=mod, dec=dec)
    return val


def metade(val, fmt=True, mod='R$', dec=2):
    """
        -> Divide um valor pela metade
        :param val:valor a ser dividido pela metade
        :param fmt:indica se o valor será formatado para moeda ou não (padrão = True)
        :param moeda:moeda para qual o valor será formatado (padrão = R$)
        :param dec:número de casas decimais a serem mostradas (padrão = 2)
        :return:retorna o valor dividido pela metade
    """
    val /= 2
    if fmt:
        return moeda(val=val, mod=mod, dec=dec)
    return val


def resumo(val, porcAum, porcDim, fmt=True, mod='R$', dec=2):
    """
        -> Imprime o valor recebido, este aumentado de uma porcentagem, diminuido de outra porcentagem, dobrado e dividido pela metade
        :param val:valor a ser aumentado
        :param porcAum:porcentagem de quanto o valor deve ser aumentado (13 para 13%, 10 para 10%, etc)
        :param porcDim:porcentagem de quanto o valor deve ser diminuido (13 para 13%, 10 para 10%, etc)
        :param fmt:indica se o valor será formatado para moeda ou não (padrão = True)
        :param moeda:moeda para qual o valor será formatado (padrão = R$)
        :param dec:número de casas decimais a serem mostradas (padrão = 2)
    """
    print(f"+{'-'*48}+")
    print(f'|{"Resumo do Valor":^48}|')
    print(f"+{'-'*48}+")
    if fmt:
        print(f'| Preço analisado:     {moeda(val=val, mod=mod, dec=dec):>25} |')
    else:
        print(f'| Preço analisado:     {val:>25} |')
    print(f'| Dobro do preço:      {dobro(val=val, fmt=fmt, mod=mod, dec=dec):>25} |')
    print(f'| Metade:              {metade(val=val, fmt=fmt, mod=mod, dec=dec):>25} |')
    print(f'| {porcAum:>3}% de aumento:    {aumentar(val=val, porc=porcAum, fmt=fmt, mod=mod, dec=dec):>25} |')
    print(f'| {porcDim:>3}% de diminuição: {diminuir(val=val, porc=porcDim, fmt=fmt, mod=mod, dec=dec):>25} |')
    print(f"+{'-'*48}+")
