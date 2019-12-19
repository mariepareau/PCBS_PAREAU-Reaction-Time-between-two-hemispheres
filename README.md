# PCBS_PAREAU-Reaction-Time-between-two-hemispheres
## Description
Mon projet consiste à analyser le temps de réaction nécessaire pour que l'information passe d'un hémisphère à un autre.
Le sujet fixera un croix de fixation au centre de l'écran tout le long de l'expérience. Il apparaitra un symbole à gauche où à droite de l'écran. Le symbole pourra apparaitre dans un intervalle de temps de 1 à 10 secondes. Il devra appuyer sur la touche "A" ou "P" avec sa ma droite ou gauche en fonction de ce qui lui sera demandé au début de chaque bloc.
Il y aura donc quatre conditions :
-le symbole apparait à droite et il doit répondre avec la main droite ("P") : ipsilatétal
-le symbole apparait à gauche et il doit répondre avec la main droite ("P") : controlatéral
-le symbole apparait à gauche et il doit répondre avec la main gauche ("A") : ipsilatéral
-le symbole apparait à gauche et il doit répondre avec la main droite ("A") : controlatéral


J'essaye pour l'instant de faire apparaitre une croix au centre de l'écran qui restera tout au long de l'experimentation.
J'importe random, numpy et expyriment

import random
import expyriment
from expyriment import stimuli, design, control

exp = design.Experiment("Projet PCBS")
control.initialize(exp)
screen_size = exp.screen.surface.get_size()
user_device = exp.keyboard

Je définis les paramètres de la croix de fixation

fixcross = stimuli.FixCross(size=(15, 15), line_width = 3)
fixcross.preload()
Blankscreen = stimuli.BlankScreen()

Je fais apparaitre la croix

for trial in range(10):
	     show_time = random.randint(1000,2000)
	     fixcross.present(update=True)
	     exp.clock.wait(show_time)
