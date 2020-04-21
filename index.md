Bienvenue au cours de Python du DU Bii. Vous trouverez sur ce dépôt toutes les informations et ressources nécessaires.

=======
## Intervenants

1. Patrick Fuchs, Université de Paris, `<patrick.fuchs@u-paris.fr>` (co-responsable)
2. Sandra Dérozier, INRAE, `<sandra.derozier@inra.fr>` (co-responsable)
3. Pierre Poulain, Université de Paris, `<pierre.poulain@u-paris.fr>`
4. Hubert Santuz, CNRS, `<hubert.santuz@gmail.com>`


## Prérequis

Dans un premier temps, nous vous suggérons d'apprendre les bases de Python sur le site de DataCamp.

Cours [Introduction to Python](https://www.datacamp.com/courses/intro-to-python-for-data-science) sur DataCamp.

Chapitres à traiter :

* Python Basics
* Python Lists
* Functions and Packages

Temps estimé : 4 heures.

Ensuite, nous vous demandons de travailler [notre ressource Python en ligne](https://python.sdv.univ-paris-diderot.fr/), en particulier les deux chapitres suivants :

[Boucles et comparaisons](https://python.sdv.univ-paris-diderot.fr/05_boucles_comparaisons/) et les exercices

* 5.4.2. Boucle et jours de la semaine
* 5.4.4. Nombres pairs et impairs
* 5.4.5. Calcul de la moyenne

[Tests](https://python.sdv.univ-paris-diderot.fr/06_tests/) et les exercices

* 6.7.1. Jours de la semaine
* 6.7.2. Séquence complémentaire d'un brin d'ADN
* 6.7.4. Fréquence des acides aminés

Temps estimé : 1 heure.

Pour la partie sur les boucles et les tests, nous vous conseillons d'utiliser le site [pythontutor](http://pythontutor.com/) qui permet de "pythonner" en ligne sans avoir à installer Python sur votre machine.

Lors du premier cours, nous vous fournirons un polycopié complet du cours. Inutile donc de l'imprimer de votre côté.

## Synopsis

Dans ce cours, nous allons voir les bases du langage Python. Au-delà de l'apprentissage de la syntaxe du langage Python, nous allons voir progressivement quelques bases d'algorithmie, c'est-à-dire comment transformer un problème énoncé en français, en une suite d'instructions informatiques.

L'apprentissage de la programmation est un processus nécessitant un certain investissement. Ainsi, nous vous conseillons de faire un maximum d'exercices sur une base régulière afin d'acquérir certains automatismes. 

A la fin du cours, vous devriez être capable d'écrire des scripts de base permettant de :

- lire des fichiers contenant des données biologiques et rechercher des contenus spécifiques dans ces fichiers ;
- changer le format d'un fichier en un autre ;
- faire des calculs de base sur les données extraites des fichiers ;
- réaliser une suite de tâches plus ou moins complexes ;
- avoir les bases pour continuer à vous former par vous même après la fin du DU.

En outre, vous apprendrez à :
- utiliser des modules incontournables en analyse de données (pandas, numpy, matplolib) ;
- utiliser et concevoir des *notebooks* Jupyter.

## Organisation des cours

Les enseignements seront donnés sous forme de cours / TP, quelques minutes de théorie en *live coding* seront suivies d'une mise en pratique immédiate. 

A titre indicatif, nous détaillons dans la suite le découpage des différentes séances. Ce découpage est succeptible de changer en fonction du degré d'avancement de l'ensemble des stagiaires. N'hésitez pas à revenir régulièrement sur cette page pendant la formation.

### Séance 1

Mardi 3 mars : 9h30 - 12h30

Instructeurs : Patrick Fuchs et Sandra Dérozier ; helper : Hubert Santuz

Révisions des bases travaillées en autonomie (variables, listes, boucles, comparaisons, tests).

**Corrections des exercices**

Les corrections des exercices se trouvent sur [Moodle](https://moodlesupd.script.univ-paris-diderot.fr/mod/folder/view.php?id=171492).

**Liens vers des articles intéressants**

* Lien vers une [interview de Guido van RossumURL](https://lemonde.fr/pixels/article/2018/07/25/je-n-imaginais-pas-que-python-connaitrait-un-tel-succes_5335917_4408996.html)
* Un article intéressant qui montre l'importance de la programmation en biologie et qui évoque Python bien sûr ! [Ten simple rules for biologists learning to programURL](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005871)

**Un peu de travail pour la prochaine séance**

* lire le chapitre **[3.2. Ecriture formatée](https://python.sdv.univ-paris-diderot.fr/03_affichage/#32-ecriture-formatee)**
* faire les exercices sur l'**écriture formatée** ([3.5.1 à 3.5.5](https://python.sdv.univ-paris-diderot.fr/03_affichage/#35-exercices))
* faire les exercices sur les **boucles** ([5.4.1 à 5.4.9](https://python.sdv.univ-paris-diderot.fr/05_boucles_comparaisons/#54-exercices))

### Séance 2

Mercredi 4 mars : 14h30 - 17h30

Instructeurs : Patrick Fuchs et Sandra Dérozier ; helper : Hubert Santuz

Consolidation des bases (boucles, tests), fichiers, modules.

**Session de cours**

Voici la [session de cours sur les boucles et tests](data/session_python_2020-03-04_apm_readable.txt).

**Corrections des exercices**

Les corrections des exercices se trouvent sur [Moodle](https://moodlesupd.script.univ-paris-diderot.fr/mod/folder/view.php?id=171492).

**Arithmétique des floats**

Si vous souhaitez comprendre pourquoi [l'arithmétique des floats est limitée à une certaine précision](https://docs.python.org/3/tutorial/floatingpoint.html).

**Un peu de travail pour la prochaine séance**

* lire le chapitre **[7. Fichiers](https://python.sdv.univ-paris-diderot.fr/07_fichiers/)**
* lire le chapitre **[8. Modules](https://python.sdv.univ-paris-diderot.fr/08_modules/)**
* faire les exercices sur les **boucles** ([5.4.10](https://python.sdv.univ-paris-diderot.fr/05_boucles_comparaisons/#5410-pyramide) et [5.4.11](https://python.sdv.univ-paris-diderot.fr/05_boucles_comparaisons/#5411-parcours-de-matrice))
* faire un exercice sur les **tests** ([6.7.9 méthode 1](https://python.sdv.univ-paris-diderot.fr/06_tests/#methode-1-peu-optimale-mais-assez-intuitive))
* faire les exercices sur les **fichiers** ([7.7.1](https://python.sdv.univ-paris-diderot.fr/07_fichiers/#771-moyenne-des-notes), [7.7.2](https://python.sdv.univ-paris-diderot.fr/07_fichiers/#772-admis-ou-recale) et [7.7.3](https://python.sdv.univ-paris-diderot.fr/07_fichiers/#773-spirale-exercice))

### Séance 3

Jeudi 12 mars : 13h30 - 16h30

Instructeurs : Pierre Poulain et Patrick Fuchs ; helper : Hubert Santuz

Fichiers, Modules, [Jupyter & Matplotlib](https://cupnet.net/intro-jupyter-dubii/).

**Corrections exercices**

- [pyramide avec opérateur de formatage](data/pyramides.py) ou [pyramide en calculant le nombre d'espaces et d'étoiles](data/pyramides2.py)
- [parcours de matrice](data/parcours_matrice.py)

**Session de cours**

Voici la [session de cours sur les fichiers et les modules](data/session_python_2020-03-12_apm_readable.txt).

**Un peu de travail pour la prochaine séance**

- Refaire le [TP sur Jupyter](https://cupnet.net/intro-jupyter-dubii/)
- [Exo 5.4.12](https://python.sdv.univ-paris-diderot.fr/05_boucles_comparaisons/#5412-parcours-de-demi-matrice-sans-la-diagonale-exercice) Parcours de demi-matrice sans la diagonale
- [Exo 6.7.9 (méthode 2)](https://python.sdv.univ-paris-diderot.fr/06_tests/#methode-2-plus-optimale-et-plus-rapide-mais-un-peu-plus-compliquee) Détermination des nombres premiers inférieurs à 100
- [Exo 8.7.9](https://python.sdv.univ-paris-diderot.fr/08_modules/#879-determination-du-nombre-pi-par-la-methode-monte-carlo-exercice) Détermination du nombre pi par la méthode Monte-Carlo ; si vous vous sentez capable, vous pouvez essayer de faire l'exercice dans un notebook jupyter et de faire un plot inspiré de la [page Wikipedia sur le Monte-Carlo](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Pi_30K.gif/440px-Pi_30K.gif) : les points dans le cercle en rouge, les points or du cercle en bleu. Vous pouvez utiliser pour cela la fonction `plt.scatter(x, y)`. Cette fonction dessine un nuage de points dans un graphe, par exemple :

```
import matplotlib.pyplot as plt

x = [1, 3, 4, 4, 7, 8, 2, 5, 7, 2]
y = [8, 9, 1, 2, 9, 4, 2, 2, 2, 8]

plt.scatter(x,y)
plt.show() # inutile dans un notebook, obligatoire dans un script lancé dans un shell
```

- Lire les chapitres [10 Plus sur les chaînes de caractères](https://python.sdv.univ-paris-diderot.fr/10_plus_sur_les_chaines_de_caracteres/) et [11 Plus sur les listes](https://python.sdv.univ-paris-diderot.fr/11_plus_sur_les_listes/)
- Faire le [QCM d'entraînement](https://moodlesupd.script.univ-paris-diderot.fr/mod/quiz/view.php?id=225633)

### Exercices pour ne pas perdre la main pendant le confinement

#### Correction du Monte-Carlo pour la détermination du nombre pi

Le notebook corrigeant l'exo 8.7.9 est [ici pour le regarder](https://github.com/DU-Bii/module-2-Python/blob/master/data/pi_MC.ipynb), pour le télécharger c'est [ici](data/pi_MC.ipynb).

#### Exo du 3 avril 2020

Télécharger la séquence du [génome du SARS-COV2 au format fasta](https://www.ncbi.nlm.nih.gov/nuccore/MN908947.3?report=fasta). Dans le même répertoire, créer un script nommé `compo_sars_cov2.py` qui calcule la composition en ATGC de ce génome. Voici les différentes étapes proposées :
- Ouvrir le fichier en lecture avec `with` et récupérer la séquence dans une chaine de caractères `seq` ;
- Attention à ne pas récupérer la première ligne qui commence par le caractère `>` (tiens n'y avait-il pas une méthode pour ça dans le chapitre 10 ;-) ???) ;
- Attention à chaque ligne il vous faudra enlever le retour à la ligne (*hint* la méthode `.strip()` est votre amie, cf. chapitre 10 ;-) !) ;
- Une fois la séquence récupérée, faire une boucle sur tout le génome et calculer le nombre de ATGC ;
- Au final on souhaite la sortie suivante (où vous remplacerez les X par les vraies valeurs) :

```
La longueur du génome est XXXXX bases
nbA =  XXXX bases ; %age A = XX.XX %
nbT =  XXXX bases ; %age T = XX.XX %
nbG =  XXXX bases ; %age G = XX.XX %
nbC =  XXXX bases ; %age C = XX.XX %
```
- Ainsi qu'un graphe en batons avec matplotlib du pourcentage d'ATGC.

*Pour les warriors* : vous pouvez faire ça dans un notebook jupyter !

#### Exo du 21 avril 2020

Sur la base de l'exercice précédent, on se propose de faire une représentation du génome du SARS-COV2 en [chaos game](https://en.wikipedia.org/wiki/Chaos_game). Cette méthode de représentation basée sur les fractales comme le [triangle de Sierpinski](https://fr.wikipedia.org/wiki/Triangle_de_Sierpi%C5%84ski) permet d'avoir une vision d'un génome en un coup d'oeil ([ici](http://www.cs.gettysburg.edu/~ilinkin/projects/bio/chaosgame/home.html) un exemple).

Voici l'algorithme du chaos game appliqué à une séquence d'ADN :

- Soit une séquence d’ADN seq de longueur suffisante (> 10000 pb)
- Soit un espace carré où les 4 sommets de ce carré représentent les 4 bases ATGC
- Au départ, on se place au milieu du carré
- On lit la séquence nucléotide par nucléotide
  - A chaque nucléotide lu, on se déplace au centre du segment entre la position actuelle et le sommet représentant le nucléotide actuellement lu

Un exemple est illustré ci-dessous sur le début d’une séquence d’ADN :

![](img/chaos_game.png)

Comme montré dans le schéma, on pourra arbitrairement décider que le C possède les coordonnées (0,0), G(1,0), A(0,1) et T (1,1). Pour tracer les points, vous pourrez utiliser la fonction `plt.scatter()` de matplotlib (cf. exo de calcul de Pi par Monte-Carlo).

Conseils : 

- Faites-vous la main sur une séquence très courte, puis une fois que ça fonctionne passez sur le génome du virus.
- Une pixelle représente un nucléotide, on utilise la même couleur pour toute les pixelles. Chaque pixelle doit être très petite : avec la fonction `plt.scatter()`, utilisez les arguments `s=1` (*size*) et `linewidth=0`.
- Si vous mettez une instruction `plt.scatter(x, y)` à chaque itération de la boucle principale, le code sera très long à tourner pour le génome du virus (> 10'). Stockez plutôt les coordonnées *x* et *y* de vos points dans des listes puis passez ces listes comme argument à la fonction `plt.scatter()` une fois la boucle principale terminée.

Bien sûr vous pouvez vous amuser à faire l'exercice dans un notebook Jupyter :wink:.

Pour aller un peu plus loin sur le chaos game, voici un [article](https://doi.org/10.1093/oxfordjournals.molbev.a026048) faisant le tour de la technique.

### Séance 4

Initialement prévue le Mardi 24 mars : 9h30 - 12h30

Instructeurs : Patrick Fuchs et Sandra Dérozier

Plus sur les chaînes de caractères. Plus sur les listes. Numpy (calculs numériques).

### Séance 5

Initialement prévue le Mardi 24 mars : 14h30 - 17h30

Instructeurs : Patrick Fuchs et Sandra Dérozier ; helper : Pierre Poulain

Dictionnaires/tuples, pandas (manipulation & analyse de données).

### Séance 6

Initialement prévue le Jeudi 26 mars : 9h - 12h

Instructeurs : Pierre Poulain, Sandra Dérozier & Patrick Fuchs ; helper : Hubert Santuz

Cas d’applications.

## Accès

- Github: <https://github.com/DU-Bii/module-2-Python>

## License

![](img/CC-BY-SA.png)

This content is released under the [Creative Commons Attribution-ShareAlike 4.0 ](https://creativecommons.org/licenses/by-sa/4.0/deed.en) (CC BY-SA 4.0) license. See the bundled [LICENSE](LICENSE.txt) file for details.

Ce contenu est mis à disposition selon les termes de la licence [Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) (CC BY-SA 4.0). Consultez le fichier [LICENSE](LICENSE.txt) pour plus de détails.
