def lerArquivo(arq='texto.txt'):
    """
        -> Imprime as linhas de um arquivo txt
        :param arq:arquivo de texto a ser lido, caso não seja informado será considerado o arquivo texto.txt
    """
    try:
        arquivo = open(arq, 'r')
        for i in arquivo:
            print(i, end='')
    except FileNotFoundError:
        from auxiliar import color
        print(f"{color('vermelho')}Erro: O arquivo {arq} não foi encontrado{color()}")
    except:
        from auxiliar import color
        print(f"{color('vermelho')}Erro: Não foi possível ler o arquivo {arq}{color()}")
        arquivo.close()
    else:
        arquivo.close()


def inserirEmArquivo(arq='texto.txt', nome='', idade=''):
    """
        -> Insere nome e idade em arquivo txt
        :param arq:arquivo de texto onde será inserida a linha, caso não seja informado será considerado o arquivo texto.txt
        :param nome:nome a ser inserido, caso não seja informado será considerado uma linha em branco
        :param idade:idade a ser inserida, caso não seja informada será considerada uma linha em branco
    """
    try:
        arquivo = open(arq, 'r')
        conteudo = arquivo.readlines()
        conteudo.append(f'\n\t  {nome:<35}{idade:>8} anos')
        arquivo = open(arq, 'w')
        arquivo.writelines(conteudo)
    except FileNotFoundError:
        from auxiliar import color
        print(f"{color('vermelho')}Erro: O arquivo {arq} não foi encontrado{color()}")
    except:
        from auxiliar import color
        print(f"{color('vermelho')}Erro: Não foi possível inserir no arquivo {arq}{color()}")
        arquivo.close()
    else:
        from auxiliar import color
        print(f"{color('verde')}Pessoa inserida com sucesso{color()}")
        arquivo.close()
