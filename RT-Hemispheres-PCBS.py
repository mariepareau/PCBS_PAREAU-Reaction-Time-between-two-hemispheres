# Combien de temps met l'information pour circuler d'un hemisphère à l'autre ?

import random
import expyriment
from expyriment import stimuli, design, control

exp = design.Experiment("Projet PCBS")
control.initialize(exp)
screen_size = exp.screen.surface.get_size()
user_device = exp.keyboard

## Stimulus
circle_dist = 200
circle_radius = 20
left_circle = stimuli.Circle(circle_radius, position=[-circle_dist, 0])
left_circle.preload()
right_circle = stimuli.Circle(circle_radius, position=[circle_dist, 0])
right_circle.preload()
circle_displaytime = 100

## Fixcross
fixcross = stimuli.FixCross(size=(15, 15), line_width = 3)
fixcross.preload()
Blankscreen = stimuli.BlankScreen()

## Instruction
instruction = """ Block 1 \n\
Fixez  la croix de fixation. \n\
Positionnez  votre index droit sur la flèche droite du clavier et votre index gauche sur la flèche gauche du clavier. \n\
Appuyez  avec la flèche droite quand le rond blanc apparait à droite et appuyez avec la flèche gauche quand il apparait à gauche. \n\
Appuyez  sur Enter pour commencer."""

stimuli.TextScreen("Condition Ipsilatérale", instruction).present()
exp.keyboard.wait()

## Block Ipsilatéral
block_one = expyriment.design.Block(name="Ipsilatéral")
trial_one = expyriment.design.Trial()
stim = left_circle
stim.preload()
trial_one.add_stimulus(stim)
trial_two = expyriment.design.Trial()
stim = right_circle
trial_two.add_stimulus(stim)
trial_three = expyriment.design.Trial()
stim = right_circle
trial_three.add_stimulus(stim)
trial_four = expyriment.design.Trial()
stim = left_circle
trial_four.add_stimulus(stim)
trial_five = expyriment.design.Trial()
stim = right_circle
trial_five.add_stimulus(stim)
trial_six = expyriment.design.Trial()
stim = left_circle
trial_six.add_stimulus(stim)
block_one.add_trial(trial_one)
block_one.add_trial(trial_two)
block_one.add_trial(trial_three)
block_one.add_trial(trial_four)
block_one.add_trial(trial_five)
block_one.add_trial(trial_six)
exp.add_block(block_one)

expyriment.control.start()

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()
        key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
                                     expyriment.misc.constants.K_RIGHT])
        exp.data.add([block.name, trial.id, key, rt])

expyriment.control.end()

instruction2 = """Block 2 \n\
Fixez la croix de fixation. \n\
Positionnez votre index droit sur la flèche gauche du clavier et votre index gauche sur la flèche droite du clavier. \n\
Appuyez avec la flèche droite quand le rond blanc apparait à droite et appuyez avec la flèche gauche quand il apparait à gauche.
Appuyer sur Enter pour commencer."""

stimuli.TextScreen("Condition Controlatérale", instruction2).present()
exp.keyboard.wait()

## Block Controlatéral
block_two = expyriment.design.Block(name="Controlatéral")
trial_one = expyriment.design.Trial()
stim = right_circle
stim.preload()
trial_one.add_stimulus(stim)
trial_two = expyriment.design.Trial()
stim = left_circle
trial_two.add_stimulus(stim)
trial_three = expyriment.design.Trial()
stim = right_circle
trial_three.add_stimulus(stim)
trial_four = expyriment.design.Trial()
stim = left_circle
trial_four.add_stimulus(stim)
trial_five = expyriment.design.Trial()
stim = right_circle
trial_five.add_stimulus(stim)
trial_six = expyriment.design.Trial()
stim = right_circle
trial_six.add_stimulus(stim)
block_two.add_trial(trial_one)
block_two.add_trial(trial_two)
block_two.add_trial(trial_three)
block_two.add_trial(trial_four)
block_two.add_trial(trial_five)
block_two.add_trial(trial_six)
exp.add_block(block_two)

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()
        key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
                                     expyriment.misc.constants.K_RIGHT])
        exp.data.add([block.name, trial.id, key, rt])

expyriment.control.end()


#fix cross
fixcross = stimuli.FixCross(size=(15, 15), line_width = 3)
fixcross.preload()
Blankscreen = stimuli.BlankScreen()

for trial in block.trials:
	     show_time = random.randint(1000,2000)
	     fixcross.present(update=True)
	     exp.clock.wait(show_time)
