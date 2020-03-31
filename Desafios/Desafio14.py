import os

t = float(input('Digite a temperatura em °C: '))
print('{}°C equivale a {}°F'.format(t, (t * (9/5)) + 32))

os.system('pause')
