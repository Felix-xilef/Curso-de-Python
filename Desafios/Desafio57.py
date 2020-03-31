sexo = input('\n\tDigite o seu sexo (M / F): ').strip().lower()
while (sexo != 'm') and (sexo != 'f'):
    sexo = input("""
    \t !!!!! SEXO INVÁLIDO !!!!!
    \t Digite:
    \t  • M para masculino
    \t  • F para feminino
    
    \tDigite o seu sexo (M / F): """).strip().lower()

input('\n\nPressione <enter> para continuar')
