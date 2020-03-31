from os import system

# No terminal do PyCharm ou VSCode:
#
# \ (contra barra) - para começar código ANSI
# 033 - significa que é para cor
# [ (colchete)
# x - código para o style (x =  - padrão; x = 0 - nenhum; x = 1 - bold; x = 4 - underline; x = 7 - negative)
# ; (ponto e vírgula)
# y - código para o text (y =  - padrão; y = 30 - branco; y = 31 - vermelho; y = 32 - verde; y = 33 - amarelo; y = 34 - azul; y = 35 - magenta;
# ; (ponto e vírgula)                                                                                            y = 36 - ciano; y = 37 - cinza)
# z - código para o back (z =  - padrão; y = 40 - branco; y = 41 - vermelho; y = 42 - verde; y = 43 - amarelo; y = 44 - azul; y = 45 - magenta;
# m (letra 'm')                                                                                                  y = 46 - ciano; y = 47 - cinza)
# \033[x;y;zm
# • Exemplo:
#           \033[0;30;41m (\033[30;41m)
#           \033[4;33;44m
#           \033[1;35;43m
#           \033[0;30;42m (\033[30;42m)
#           \033[0;0;0m  (\033[m)
#           \033[7;30;0m  (\033[7;30m)

print('\033[34mOlá, \033[33mMundo!\033[m')

system('pause')
