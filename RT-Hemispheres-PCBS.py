# Combien de temps met l'information pour circuler d'un hemisphère à l'autre ?

import random
import expyriment
from expyriment import stimuli, design, control

exp = design.Experiment("Projet PCBS")
control.initialize(exp)
screen_size = exp.screen.surface.get_size()
user_device = exp.keyboard

fixcross = stimuli.FixCross(size=(15, 15), line_width = 3)
fixcross.preload()
Blankscreen = stimuli.BlankScreen()

for trial in range(10):
	     show_time = random.randint(1000,2000)
	     fixcross.present(update=True)
	     exp.clock.wait(show_time)


import pygame 
screen = pygame.display, pygame.DOUBLEBUF)
pygame.draw.circle(screen, RED, (400, 200), 50, 0)
pygame.display.flip()
pygame.image.save(screen, "circle-red.png")




J'arrive à faire une croix de fixation sur expyriment. Et j'arrive à coder un cercle rouge sur
pygame. je n'arrive pas à mettre les deux ensemble c'est à dire faire apparaitre le cercle dans expyriment
est ce possible ? Ou dois je coder différemment mon cercle pour qu'il soit visible sur expyriment ?
