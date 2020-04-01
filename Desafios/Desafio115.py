from auxiliar import color
from Desafio115Arquivo import lerArquivo, inserirEmArquivo

# main
linha = f"{color('amarelo')}{'-'*50}{color()}"
menu = f"""
\t{linha}{color('azul')}
\t{'Menu Principal':^50}
\t{linha}
\t  {color('amarelo')}1{color('verde')} -{color('azul')} Ver pessoas cadastradas
\t  {color('amarelo')}2{color('verde')} -{color('azul')} Cadastrar nova Pessoa
\t  {color('amarelo')}3{color('verde')} -{color('azul')} Sair do Sistema
\t{linha}{color('azul')}
\t  Digite uma opção: {color('verde')}"""

while True:
    try:
        op = int(input(menu))
        print(color(), end='')
    except:
        print(f"\t{color('vermelho')}ERRO: Digite uma opção válida!{color()}")
    else:
        if op == 1:
            print(f"\n\t{linha}\n\t{color('azul')}{'Pessoas Cadastradas':^50}\n\t{linha}", end='')
            lerArquivo('Desafio115Cadastro.txt')
        elif op == 2:
            print(f"\n\t{linha}\n\t{color('azul')}{'Novo Cadastro':^50}\n\t{linha}{color('azul')}")
            nome = str(input(f'\t  Nome:{color()}'))
            while True:
                try:
                    idade = int(input(f"\t{color('azul')}  Idade:{color()} "))
                except:
                    print(f"\t{color('vermelho')}ERRO: Digite uma idade válida!{color()}")
                else:
                    break
            inserirEmArquivo('Desafio115Cadastro.txt', nome=nome, idade=idade)
        elif op == 3:
            break
        else:
            print(f"\t{color('vermelho')}ERRO: Digite uma opção válida!{color()}")
