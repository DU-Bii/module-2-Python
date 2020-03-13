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

Consolidation des bases, fichiers, modules.

** Session de cours **

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

** Corrections exercices **

- [pyramide avec opérateur de formatage](data/pyramides.py) ou [pyramide en calculant le nombre d'espaces et d'étoiles](data/pyramides2.py)
- [parcours de matrice](data/parcours_matrice.py)

** Session de cours **

Voici la [session de cours sur les fichiers et les modules](data/session_python_2020-03-12_apm_readable.txt).

Fichiers, Modules, [Jupyter & Matplotlib](https://cupnet.net/intro-jupyter-dubii/).

**Un peu de travail pour la prochaine séance**

- Refaire le TP sur Jupyter
- Exo 5.4.12 Parcours de demi-matrice sans la diagonale
- Exo 6.7.9 (méthode 2) Détermination des nombres premiers inférieurs à 100
- Exo 8.7.9 Détermination du nombre pi par la méthode Monte-Carlo ; si vous vous sentez capable, vous pouvez essayer de faire l'exercice dans un notebook jupyter et de faire un plot inspiré de la [page Wikipedia sur le Monte-Carlo](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Pi_30K.gif/440px-Pi_30K.gif) : les points dans le cercle en rouge, les points or du cercle en bleu. Vous pouvez utiliser pour cela la fonction `plt.scatter(x, y)`. Cette fonction dessine un nuage de points dans un graphe, par exemple :

```
import matplotlib.pyplot as plt

x = [1, 3, 4, 4, 7, 8, 2, 5, 7, 2]
y = [8, 9, 1, 2, 9, 4, 2, 2, 2, 8]

plt.scatter(x,y)
plt.show() # inutile dans un notebook, obligatoire dans un script lancé dans un shell
```

- Lire les chapitres 10 (Plus sur les chaînes de caractères) et chapitres 11 (Plus sur les listes)


### Séance 4

Mardi 24 mars : 9h30 - 12h30

Instructeurs : Patrick Fuchs et Sandra Dérozier

Plus sur les chaînes de caractères. Plus sur les listes. Numpy (calculs numériques).

### Séance 5

Mardi 24 mars : 14h30 - 17h30

Instructeurs : Patrick Fuchs et Sandra Dérozier ; helper : Pierre Poulain

Dictionnaires/tuples, pandas (manipulation & analyse de données).

### Séance 6

Jeudi 26 mars : 9h - 12h

Instructeurs : Pierre Poulain, Sandra Dérozier & Patrick Fuchs ; helper : Hubert Santuz

Cas d’applications.

## Accès

- Github: <https://github.com/DU-Bii/module-2-Python>

## License

![](img/CC-BY-SA.png)

This content is released under the [Creative Commons Attribution-ShareAlike 4.0 ](https://creativecommons.org/licenses/by-sa/4.0/deed.en) (CC BY-SA 4.0) license. See the bundled [LICENSE](LICENSE.txt) file for details.

Ce contenu est mis à disposition selon les termes de la licence [Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) (CC BY-SA 4.0). Consultez le fichier [LICENSE](LICENSE.txt) pour plus de détails.
