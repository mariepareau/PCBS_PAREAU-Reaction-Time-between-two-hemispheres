
import random
import numpy as np
import expyriment
from expyriment import stimuli, design, control

exp = design.Experiment("Projet PCBS")
control.initialize(exp)
screen_size = exp.screen.surface.get_size()
user_device = exp.keyboard

## Création de la fonction display-circle
def display_circle(n, block, expected):
    for i in range(n):
        side = random.randint(0,1)
        expected[i] = side
        if side == 0:
            stim = left_circle
            stim.preload()
            trial = expyriment.design.Trial()
            trial.add_stimulus(stim)
            block.add_trial(trial)
        else:
            stim = right_circle
            stim.preload()
            trial = expyriment.design.Trial()
            trial.add_stimulus(stim)
            block.add_trial(trial)


## Stimulus
n = 10
expected_block_one = np.zeros(n)
expected_block_two = np.zeros(n)
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

## Instruction
instruction1 = """ Block 1 \n\
Fixez  la croix de fixation. \n\
Positionnez  votre index droit sur la flèche droite du clavier et votre index gauche sur la flèche gauche du clavier. \n\
Appuyez  avec la flèche droite quand le rond blanc apparait à droite et appuyez avec la flèche gauche quand il apparait à gauche. \n\
Appuyez sur une des flèches pour commencer."""


instruction2 = """Block 2 \n\
Fixez la croix de fixation. \n\
Positionnez votre index droit sur la flèche gauche du clavier et votre index gauche sur la flèche droite du clavier. \n\
Appuyez avec la flèche droite quand le rond blanc apparait à droite et appuyez avec la flèche gauche quand il apparait à gauche.
Appuyer sur une des flèches pour commencer."""


## Bloc Ipsilatéral
block_one = expyriment.design.Block(name="Ipsilatéral")
display_circle(n, block_one, expected_block_one)
exp.add_block(block_one)

## Bloc Controlatéral
block_two = expyriment.design.Block(name="Controlatéral")
display_circle(n, block_two, expected_block_two)
exp.add_block(block_two)


expyriment.control.start()
# Main loop
for block in exp.blocks:
    if block.name == 'Ipsilatéral':
        stimuli.TextScreen("Condition Ipsilatérale", instruction1).present()
        exp.keyboard.wait()
        fixcross.present(clear = False)
        for trial in block.trials:
            fixcross.present()
            trial.stimuli[0].present(clear = False)
            key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
                                         expyriment.misc.constants.K_RIGHT])
            fixcross.present(clear = False)
# Identify each key to its corresponding position
            if key == 276:
                results = 'gauche'
            elif key == 275:
                results = 'droite'
            #Compare to expected position
            if expected_block_one[trial.id] == 1:
                expected = 'droite'
            else:
                expected = 'gauche'
            # Save results
            exp.data.add([block.name, trial.id, expected, results, rt])
    else:
        stimuli.TextScreen("Condition Controlatérale", instruction2).present()
        exp.keyboard.wait()
        fixcross.present(clear = False)
        for trial in block.trials:
            fixcross.present()
            trial.stimuli[0].present(clear = False)
            key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
                                         expyriment.misc.constants.K_RIGHT])
            fixcross.present(clear = False)
            # Identify each key to its corresponding position
            if key == 276:
                results == 'gauche'
            elif key == 275:
                results = 'droite'
            #Compare to expected position
            if expected_block_two[trial.id] == 1:
                expected = 'droite'
            else:
                expected = 'gauche'
            #Save results
            exp.data.add([block.name, trial.id, expected, results, rt])

expyriment.control.end()
