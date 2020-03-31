def leiaDinheiro(msg):
    """
        -> Valida a entrada de um valor monetário, isto é de um float com vírgula ou ponto, pelo teclado
        :param msg:mensagem que será impressa na tela para a entrada de dados
        :return:valor recebido
    """
    while True:
        numReal = False
        virgPont = 0
        
        resp = input(msg)
        #input(f'{not resp}')

        if resp.isnumeric():
            numReal = True
        elif not resp.isalpha():
            numReal = True
            for i in resp:
                if i in ',.':
                    virgPont += 1
                    if virgPont > 1:
                        numReal = False
                        break
                    elif i == ',':
                        resp = resp.replace(',', '.')
                elif not i.isnumeric():
                    numReal = False
                    break
        
        if numReal and (resp not in '.,') and resp != '':
            return float(resp)
        
        print('!!! Valor Inválido !!!')
