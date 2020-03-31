from os import system
from time import sleep

print("""
\t -----------------------------------
\t   CONTAGEM DOS FOGOS DE ARTIFÍCIO 
\t -----------------------------------""")
for i in range(10, -1, -1):
    sleep(1)
    print('\t                  {}'.format(i))
print("""\t -----------------------------------
\t         !!! LANÇAR FOGOS !!!
\t -----------------------------------\n""")

system('pause')
