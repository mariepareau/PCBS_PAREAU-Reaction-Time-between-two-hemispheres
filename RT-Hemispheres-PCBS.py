# Combien de temps met l'information pour circuler d'un hemisphère à l'autre ?

import random
import expyriment
from expyriment import stimuli, design, control

exp = design.Experiment("Projet PCBS")
control.initialize(exp)
screen_size = exp.screen.surface.get_size()
user_device = exp.keyboard

#stimulus
circle_dist = 200
circle_radius = 20
left_circle = stimuli.Circle(circle_radius, position=[-circle_dist, 0])
left_circle.preload()
right_circle = stimuli.Circle(circle_radius, position=[circle_dist, 0])
right_circle.preload()
circle_displaytime = 100
right_circle.present()
left_circle.present()



#fix cross
fixcross = stimuli.FixCross(size=(15, 15), line_width = 3)
fixcross.preload()
Blankscreen = stimuli.BlankScreen()

for trial in range(10):
	     show_time = random.randint(1000,2000)
	     fixcross.present(update=True)
	     exp.clock.wait(show_time)


stimulus





#####################
block = expyriment.design.Block(name="Block 1")
trial = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="Hello World")
stim.preload()
trial.add_stimulus(stim)
block.add_trial(trial)
exp.add_block(block)

expyriment.control.start()

stim.present()
exp.clock.wait(1000)

expyriment.control.end()
