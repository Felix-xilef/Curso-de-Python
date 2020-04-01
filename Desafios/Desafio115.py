from auxiliar import color
from Desafio115Pacote.Arquivo import lerArquivo, inserirEmArquivo
from Desafio115Pacote.Menu import menu, cabecalho, erro

# main
while True:
    try:
        mensagem = menu('Menu Principal', 'Digite uma opção: ', 'Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema')
        op = int(input(mensagem))
    except:
        print(erro('ERRO: Digite uma opção válida!'))
    else:
        if op == 1:
            print(cabecalho('Pessoas Cadastradas'))
            lerArquivo('Desafio115Cadastro.txt')
        elif op == 2:
            mensagem = cabecalho('Novo Cadastro') + f"\n\t{color('azul')}  Nome: {color()}"
            nome = input(mensagem)
            while True:
                try:
                    mensagem = f"\t{color('azul')}  Idade: {color()}"
                    idade = int(input(mensagem))
                except:
                    print(erro('ERRO: Digite uma idade válida!'))
                else:
                    break
            inserirEmArquivo('Desafio115Cadastro.txt', nome=nome, idade=idade)
        elif op == 3:
            print(color(), end='')
            break
        else:
            print(erro('ERRO: Digite uma opção válida!'))
