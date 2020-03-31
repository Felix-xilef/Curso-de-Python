def notas(*nts, sit=False):
    """
        -> Retorna um dicionário com a quantidade de notas informadas, a maior e menor nota, a média e a situação(opcional).
        :param nts:notas
        :param sit:operador para adicionar ou não a situação ao dicionário
        :return:dicionário com as informações sobre as notas
    """
    info = dict()
    info['quantidade de notas'] = len(nts)
    info['maior nota'] = max(nts)
    info['menor nota'] = min(nts)
    info['média'] = sum(nts)/len(nts)
    if sit:
        if info['média'] > 7:
            info['situação'] = 'BOA'
        elif info['média'] > 5:
            info['situação'] = 'RAZOÁVEL'
        else:
            info['situação'] = 'RUIM'
    return info


# main
print(notas(10, 5.5, 6, sit=True))

input('\n\nPressione <enter> para continuar')
