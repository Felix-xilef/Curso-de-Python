from os import system
from pygame import init, mixer, mixer_music#, event

# mixer.init()
# init()
# mixer.music.load('Desafio21.mp3')
# mixer.music.play()
# event.wait()

mixer.init()
init()
mixer_music.load('Desafio21.mp3')
mixer_music.play()

system('pause')
