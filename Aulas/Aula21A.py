# help(print)                                      • help() - mostra informações de elementos do python
# print(print.__doc__)                             • .__doc__ - mostra o documento interno do elemento do pyton

def teste2():
    print(n1, a) # printa as duas variáveis globais pois n foram "declaradas" na função


def teste():
    global a # trabalha com a variável global 'a'
    n1 = 9 # cria uma variável local com 'n1'
    a = 8
    print(n1, a)


# main
a = 2
n1 = 0
teste2()
teste()
print(n1, a)

input('\n\nPressione <enter> para continuar')
