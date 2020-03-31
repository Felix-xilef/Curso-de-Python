from auxiliar import receberInt

def voto(nasc):
    from datetime import date
    idade = int(date.today().year) - nasc
    if idade < 16:
        return f'Com {idade} anos, voto: NEGADO'
    elif idade < 18 or idade >= 60:
        return f'Com {idade} anos, voto: OPCIONAL'
    else:
        return f'Com {idade} anos, voto: OBRIGATÓRIO'


# main
nascimento = receberInt('Digite o ano de nascimento: ')
print(voto(nascimento))

input('\n\nPressione <enter> para continuar')
