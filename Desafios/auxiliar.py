def receberInt(msg = '\tDigite um número inteiro: '):
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


def receberFixo(msg, opcoes):
    """
        -> Valida a entrada de uma string pelo teclado
           *Caso a entrada seja inválida será exigida
           uma nova entrada.
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
