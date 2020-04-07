# Exercice 01 getseqfasta

Soit le fichier [UBI4_SCerevisiae.fasta](UBI4_SCerevisiae.fasta) contenant une séquence au format fasta. Ecrire un programme `getseqfasta.py`, qui lit la séquence contenue dans le fichier fasta, qui la stocke dans une chaîne de caractères nommée `sequence`. Votre programme affichera :

- le nom du fichier
- la longueur de la séquence
- un message vérifiant que le nombre de nucléotide est ou non un multiple de 3
- le nombre de codons
- les 10 premiers nucléotides
- les 10 derniers nucléotides

La sortie devrait ressembler à ça :

```
UBI4_SCerevisiae.fasta
La séquence fait XXX nucléotides
La longueur de la séquence est bien un multiple de 3 nucléotides
La séquence possède ZZZ codons
10 premiers nucléotides: YYYYYYYYYY
10 derniers nucléotides: YYYYYYYYYY
```
où `XXX` et `ZZZ` sont des entiers et `YYYYYYYYYY` sont des nucléotides. 
