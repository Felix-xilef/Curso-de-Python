try:
    a = int(input('\n\tNumerador: '))
    b = int(input('\tDenominador: '))
    r = a / b

# except: - apenas redireciona caso dê erro (GENÉRICO)
#     print('\n\tProblema encontrao') # erro - mostra erro | erro.__class__ - mostra classe do erro

except (ValueError, TypeError): # except classe: - apenas redireciona, caso dê erro da classe informada *colocar entre parêntesis e separado por vírgula caso haja mais de um erro
    print('\n\tTivemos um problema com os tipos de dados que você digitou')

except ZeroDivisionError:
    print('\n\tNão é possível dividir um número por zero!')

except KeyboardInterrupt:
    print('\n\tO usuário preferiu não informar os dados!')

except Exception as erro: # guarda a exeção na variável erro (GENÉRICO)
    print(f'\n\tProblema encontrao:\n\t{erro.__class__}') # erro - mostra erro | erro.__class__ - mostra classe do erro

else: # opcional (o que ocorrerá caso não der erro)
    print(f'\n\t{a}/{b} = {r}')

finally: # opcional (sempre é executado, isto é, caso dê ou não erro)
    print('\n\tVolte sempre! Muito obrigado!')
    input('\n\nPressione <enter> para continuar')
