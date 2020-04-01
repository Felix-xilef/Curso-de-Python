from auxiliar import color
from urllib import request

# site do pudim -> http://pudim.com.br
try:
    request.urlopen('http://pudim.com.br/')
except:
    print(f"{color('vermelho')}O site Pudim não está acessível no momento{color()}")
else:
    print(f"{color('verde')}O site Pudim está disponível{color()}")
finally:
    input('\n\nPressione <enter> para continuar')
