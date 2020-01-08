# PCBS_PAREAU-Reaction-Time-between-two-hemispheres
## Description
Mon projet consiste à analyser le temps de réaction nécessaire pour que l'information passe d'un hémisphère à un autre.
Le sujet fixera un croix de fixation au centre de l'écran tout le long de l'expérience. Il apparaitra un stimulus à gauche où à droite de l'écran. Il devra appuyer sur la touche "A" ou "P" avec sa ma droite ou gauche en fonction de ce qui lui sera demandé au début de chaque bloc.
Il y aura donc quatre conditions :
- le symbole apparait à droite et il doit répondre avec la main droite ("P") : ipsilatétal
- le symbole apparait à gauche et il doit répondre avec la main droite ("P") : controlatéral
- le symbole apparait à gauche et il doit répondre avec la main gauche ("A") : ipsilatéral
- le symbole apparait à gauche et il doit répondre avec la main droite ("A") : controlatéral
Je vais coder les conditions ipsilatérales c'est-à-dire le sujet voit le stimulus à droite et doit appuyer sur "P" et le sujet voit le stimulus à gauche et doit appuyer sur "A".



### Importation des fonctions utiles pour l'expérimentation

import random
import expyriment
from expyriment import stimuli, design, control


exp = design.Experiment("Projet PCBS")
control.initialize(exp)
screen_size = exp.screen.surface.get_size()
user_device = exp.keyboard

### Création de la croix de fixation
Le sujet doit fixer une croix de fixation tout au long de l'expérimentation.


Je définis les paramètres de la croix de fixation :

fixcross = stimuli.FixCross(size=(15, 15), line_width = 3)
fixcross.preload()
Blankscreen = stimuli.BlankScreen()

Je fais apparaitre la croix :

for trial in range(10):
	     show_time = random.randint(1000,2000)
	     fixcross.present(update=True)
	     exp.clock.wait(show_time)

### Création du stimulus visuel
Un stimulus visuel sera présenté à droite ou à gauche de la crois de fixation. Le sujet devra alors appuyer sur le "P" si l'image est apparu à droite et sur le "A" si l'image est apparu à gauche.

import pygame
pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
