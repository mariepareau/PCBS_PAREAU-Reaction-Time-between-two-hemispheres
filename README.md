# PCBS_PAREAU-Reaction-Time-between-two-hemispheres
## Description
Mon projet consiste à créer un design d'expérience pour, par la suite analyser le temps de réaction nécessaire pour que l'information passe d'un hémisphère à un autre.
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
````

### Création du stimulus visuel
Un stimulus visuel sera présenté à droite ou à gauche de la crois de fixation. Le sujet devra alors appuyer sur la flèche droite ou gauche du clavier en fonction des conditions des blocs. Dans mon code, je détaille la taille du cercle, son positionnement et le nombre de présentation du stimulus (n). Il y a un cercle à droite et un à gauche.
Je créé deux tableaux "expected..." (un pour chaque blocs) de taille n pour pouvoir sauvegarder pour chaque cercle sa position (gauche ou droite).

````
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
````

### Création des instructions
Il y aura deux instructions différentes pour les deux blocs différents : ipsilatéral et controlatéral.

#### Instruction "Bloc Ipsilatéral"
````
instruction1 = """ Block 1 \n\
Fixez  la croix de fixation. \n\
Positionnez  votre index droit sur la flèche droite du clavier et votre index gauche sur la flèche gauche du clavier. \n\
Appuyez  avec la flèche droite quand le rond blanc apparait à droite et appuyez avec la flèche gauche quand il apparait à gauche. \n\
Appuyez sur une des flèches pour commencer."""
````
#### Instruction "Bloc Controlatéral"
````
instruction2 = """Block 2 \n\
Fixez la croix de fixation. \n\
Positionnez votre index droit sur la flèche gauche du clavier et votre index gauche sur la flèche droite du clavier. \n\
Appuyez avec la flèche droite quand le rond blanc apparait à droite et appuyez avec la flèche gauche quand il apparait à gauche.
Appuyer sur une des flèches pour commencer."""
````

### Création de la fonction pour afficher le cercle à droite ou à gauche
J'ai créé une fonction qui permet d'afficher soit le cercle à droite soit le cercle à gauche. Elle prend trois arguments : n (le nombre de trial), block (numéro du bloc associé), expected (le tableau dans lequel on sauvegarde la position des cercles). La fonction random.randint permet d'afficher de manière aléatoire des objets. Dans la fonction display_circle si le 0 est tiré au sort, alors c'est le cercle gauche qui est présenté sinon c'est le cercle droit.

````
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
````

#### Affichage des instructions
Pour afficher les conditions j'écris deux lignes de code :
````
stimuli.TextScreen("Condition Controlatérale", instruction2).present()
exp.keyboard.wait()
````

### Création des blocks
Il y a deux blocs pour les deux conditions "Ipsilatérale" et "Controlatérale". Chaque bloc contient 10 trials. L'ordre de présentation des stimulus (si le cercle apparait à droite ou à gauche selon les trials) est choisi de manière aléatoire grâce à la fonction display_circle.

# Block Ipsilatéral
````
block_one = expyriment.design.Block(name="Ipsilatéral")
display_circle(n, block_one)
exp.add_block(block_one)
````

# Block Controlatéral
````
block_two = expyriment.design.Block(name="Controlatéral")
display_circle(n, block_two)
exp.add_block(block_two)
````

### expérience
````
expyriment.control.start()
````
Ici on commence la boucle principale pour afficher les instructions du bloc ipsilatéral ou controlatéral. La croix de fixation est ensuite présentée. Les stimulus préchargés grâce à la fonction display sont affichés. Les temps de réactions, les touches pressées sont enregistrés.
````
# main loop
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
````
Ensuite, j'identifie chaque touche (flèche droite ou gauche du clavier) avec la position correspondante.
````
# Identify each key to its corresponding position
            if key == 276:
                results = 'gauche'
            elif key == 275:
                results = 'droite'
````
Je récupère la position exacte du cercle pour chaque trial afin de pouvoir vérifier que le sujet ne s'est pas trompé.
````
            #compare to expected position
            if expected_block_one[trial.id] == 1:
                expected = 'droite'
            else:
                expected = 'gauche'
````
J'enregistre dans un fichier .xpd pour chaque sujet le numéro du bloc, le numéro du trial, la position attendue, la position donnée par le sujet et le temps de réaction.
````
            # save results
            exp.data.add([block.name, trial.id, expected, results, rt])
````
La même démarche est suivie pour le second bloc.
````
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
            #compare to expected position
            if expected_block_two[trial.id] == 1:
                expected = 'droite'
            else:
                expected = 'gauche'
            #save results
            exp.data.add([block.name, trial.id, expected, results, rt])

expyriment.control.end()
````

Le script complet est visualisable sur RT-Hemispheres-PCBS.py

## Conclusion

Avant ce cours mon expérience de programmation était égale à zéro. Je n'avais jamais travailler avec python et ne conceptualisais pas ce que c'était. Je ne savais pas utiliser la commande de mon ordinateur et tout le langage de programmation m'a toujours fait peur par la complexité apparente. Les exercices de bases du cours étaient difficiles pour moi et me prenais beaucoup de temps à réaliser.
Ce cours m'a permis de commencer à appréhender les concepts de programmation et certaines logiques (comme les boucles for par exemple).
Partant d'un niveau zéro, écrire ce code n'a pas été une chose facile. Il m'a d'abord fallu trouver par quoi commencer. J'ai regardé les scripts des exercices du cours portant sur le module expyriment et les temps de réaction.  Je me suis également inspiré du code d'une ancienne étudiante qui avait codé pour une tâche semblable (https://github.com/OndineS/Projet_PCBS).
Le site https://docs.expyriment.org/Tutorial.html m'a également aidé à comprendre des codes de base clairs avec lesquels j'ai ensuite travaillé.

En ce qui concerne les retours de l'UE :
- Je trouve que cette matière est une matière essentielle que j'aurais aimé commencer en licence. Avoir des groupes de niveau pourrait être plus pertinent car il est un peu intimidant de commencer à coder et poser des questions plus que basiques à côté de personne maitrisant déjà la programmation. De plus, pour les confirmés cela ne devaient pas être très stimulant de travailler à côté de personnes comme moi.
- Plus d'heures dans ce cours pourraient être également bien pour avoir le temps d'assimiler les concepts de bases avant de passer directement à la programmation d'un mini programme, ce qui me semblait insurmontable (sachant que cette année la semaine de remise à niveau était absente).
- Le cours de data camp est un peu compliqué à gérer en même temps surtout si on apprend R sur data camp et python pendant PCBS. Peut-être serait-il intéressant de les mettre à deux semestres différents ou bien de les lier : cours de PCBS pour apprendre réellement à programmer et le cours de data camp en soutien pour faire des petits exercices basiques (comme une séance de TD en soutien au cours de PCBS).
