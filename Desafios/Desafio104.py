def leiaInt(msg = '\tDigite um número inteiro: '):
    """
        -> Valida a entrada de um número inteiro pelo teclado
           *Caso a entrada seja inválida será exigida
           uma nova entrada.
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


# main
leiaInt()

input('\n\nPressione <enter> para continuar')
