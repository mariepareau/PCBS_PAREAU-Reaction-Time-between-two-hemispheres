# PCBS_PAREAU-Reaction-Time-between-two-hemispheres
## Description
Mon projet consiste à analyser le temps de réaction nécessaire pour que l'information passe d'un hémisphère à un autre.
Le sujet fixera un croix de fixation au centre de l'écran tout le long de l'expérience. Il apparaitra un stimulus à gauche où à droite de l'écran. Il devra appuyer sur la flèche droite ou sur la flèche gauche avec sa ma droite ou gauche en fonction de ce qui lui sera demandé au début de chaque bloc.
Il y aura donc quatre conditions :
- le symbole apparait à droite et il doit répondre avec la main droite : ipsilatétal
- le symbole apparait à gauche et il doit répondre avec la main droite : controlatéral
- le symbole apparait à gauche et il doit répondre avec la main gauche : ipsilatéral
- le symbole apparait à droite et il doit répondre avec la main gauche : controlatéral
J'ai décidé de réaliser deux blocs : un "Ipsilatéral" et un "Controlatéral".



### Importation des fonctions utiles pour l'expérimentation

````
import random
import expyriment
from expyriment import stimuli, design, control


exp = design.Experiment("Projet PCBS")
control.initialize(exp)
screen_size = exp.screen.surface.get_size()
user_device = exp.keyboard
````
### Création de la croix de fixation
Le sujet doit fixer une croix de fixation tout au long de l'expérimentation.


Je définis les paramètres de la croix de fixation :
````
fixcross = stimuli.FixCross(size=(15, 15), line_width = 3)
fixcross.preload()
Blankscreen = stimuli.BlankScreen()
````

Je fais apparaitre la croix :

````
for trial in range(10):
	     show_time = random.randint(1000,2000)
	     fixcross.present(update=True)
	     exp.clock.wait(show_time)
````

### Création du stimulus visuel
Un stimulus visuel sera présenté à droite ou à gauche de la crois de fixation. Le sujet devra alors appuyer sur la flèche droite ou gauche du clavier en fonction des conditions des blocs. Dans mon code, je détaille la taille du cercle, son positionnement. Il y a un cercle à droite et un à gauche.

````
circle_dist = 200
circle_radius = 20
left_circle = stimuli.Circle(circle_radius, position=[-circle_dist, 0])
left_circle.preload()
right_circle = stimuli.Circle(circle_radius, position=[circle_dist, 0])
right_circle.preload()
circle_displaytime = 100
````

### Création des instructions
Il y aura deux instructions différentes pour les deux blocs différents : ipsilatéral et controlatéral.

#### Instruction "Bloc Ipsilatéral"
````
instruction = """ Block 1 \n\
Fixez  la croix de fixation. \n\
Positionnez  votre index droit sur la flèche droite du clavier et votre index gauche sur la flèche gauche du clavier. \n\
Appuyez  avec la flèche droite quand le rond blanc apparait à droite et appuyez avec la flèche gauche quand il apparait à gauche. \n\
Appuyez  sur Enter pour commencer."""
````
#### Instruction "Bloc Controlatéral"
````
instruction2 = """Block 2 \n\
Fixez la croix de fixation. \n\
Positionnez votre index droit sur la flèche gauche du clavier et votre index gauche sur la flèche droite du clavier. \n\
Appuyez avec la flèche droite quand le rond blanc apparait à droite et appuyez avec la flèche gauche quand il apparait à gauche.
Appuyer sur Enter pour commencer."""
````
#### Affichage des instructions
Pour afficher les conditions j'écris deux lignes de code :
````
stimuli.TextScreen("Condition Controlatérale", instruction2).present()
exp.keyboard.wait()
````

### Création des blocks
Il y a deux blocks pour les deux conditions "Ipsilatérale" et "Controlatérale". Chaque block contient six trials. Je choisis moi-même l'ordre de présentation des stimulus (si le cercle apparait à droite ou à gauche selon les trials). Je me suis aidé d'un code déjà existant (celui de https://docs.expyriment.org/Tutorial.html) pour réaliser mon code.

Je créer et je nomme le bloc et le trial. Puis je choisis le stimulus que je veux faire apparaitre dans chaque trial (pour les six trials).
````
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
````
Puis j'ajoute chaque trial dans le bloc et enfin le bloc est ajouté à l'expérience.
````
block_one.add_trial(trial_one)
block_one.add_trial(trial_two)
block_one.add_trial(trial_three)
block_one.add_trial(trial_four)
block_one.add_trial(trial_five)
block_one.add_trial(trial_six)
exp.add_block(block_one)
````
La même chose est réalisée pour le deuxième bloc avec une répartition des stimulus différente.

````
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
````
### Temps de réaction

Pour récupérer les temps de réaction avec les flèches droite et gauche du clavier :
````
        key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
                                     expyriment.misc.constants.K_RIGHT])
````
Les données (numéro de bloc , de trial, la touche pressée et le temps de réaction) sont enregistrés :
````
				exp.data.add([block.name, key, rt])
````

````
expyriment.control.start()

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()
        key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
                                     expyriment.misc.constants.K_RIGHT])
        exp.data.add([block.name, trial.id, key, rt])

expyriment.control.end()
````

Le script complet est visualisable sur RT-Hemispheres-PCBS.py

## Conclusion

Avant ce cours mon expérience de programmation était égale à zéro. Je n'avais jamais travailler avec python et ne conceptualisais pas ce que c'était. Je ne savais pas utiliser la commande de mon ordinateur et tout le langage de programmation m'a toujours fait peur par la complexité apparente. Les exercices de bases du cours étaient difficiles pour moi et me prenais beaucoup de temps à réaliser.
Ce cours m'a permis de commencer à appréhender les concepts de programmation et certaines logiques (comme les boucles for par exemple).
Partant d'un niveau zéro, écrire ce code n'a pas été une chose facile. Il m'a d'abord fallu trouver par quoi commencer. J'ai regardé les scripts des exercices du cours portant sur le module expyriment et les temps de réaction.  Je me suis également inspiré du code d'une ancienne étudiante qui avait codé pour une tâche semblable (https://github.com/OndineS/Projet_PCBS).
Le site https://docs.expyriment.org/Tutorial.html m'a également aidé à avoir un code de base clair avec lequel j'ai ensuite travaillé (notamment pour le design des blocs). J'ai ainsi adapté ces codes à ma tâche en passant un long moment à comprendre la logique de chaque ligne de code puis en essayant de les modifier pour ma tâche. Après le moment de stress à l'idée de coder, il était assez ludique d'essayer de comprendre la structure du code et de le créer pour faire fonctionner mon expérience bien qu'elle soit très simple.

En ce qui concerne les retours de l'UE :
- Je trouve que cette matière est une matière essentielle que j'aurais aimé commencer en licence. Avoir des groupes de niveau pourrait être plus pertinent car il est un peu intimidant de commencer à coder et poser des questions plus que basiques à côté de personne maitrisant déjà la programmation. De plus, pour les confirmés cela ne devaient pas être très stimulant de travailler à côté de personnes comme moi.
- Plus d'heures dans ce cours pourraient être également bien pour avoir le temps d'assimiler les concepts de bases avant de passer directement à la programmation d'un mini programme, ce qui me semblait insurmontable (sachant que cette année la semaine de remise à niveau était absente).
- Le cours de data camp est un peu compliqué à gérer en même temps surtout si on apprend R sur data camp et python pendant PCBS. Peut-être serait-il intéressant de les mettre à deux semestres différents ou bien de les lier : cours de PCBS pour apprendre réellement à programmer et le cours de data camp en soutien pour faire des petits exercices basiques (comme une séance de TD en soutien au cours de PCBS).
