from os import system

velocidade = float(input('\n\tDigite a velocidade em km/h (kilometros por hora): '))
if velocidade > 80:
    print("""
    \t-- VOCÊ FOI MULTADO POR EXESSO DE VELOCIDADE --
    \t|
    \t|  Velocidade da via: 80km/h
    \t|  Velocidadde registrada: {}km/h
    \t|  Quantidade acima do limite: {}km/h
    \t|  Valor da multa: R$ {:.2f}
    \t|
    \t-----------------------------------------------\n""".format(velocidade, velocidade - 80, (velocidade - 80) * 7))

system('pause')
