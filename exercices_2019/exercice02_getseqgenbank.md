# Exercice 02 getseqgenbank

A partir du fichier genbank [NC_001133.gbk](https://python.sdv.univ-paris-diderot.fr/data-files/NC_001133.gbk) (chromosome I de levure S. Cerevisiae), on cherche à récupérer la séquence en nucléotide. Pour rappel, la séquence démarre après la ligne contenant le mot `ORIGIN` et se termine avant la ligne contenant `//` :

```
ORIGIN      
        1 ccacaccaca cccacacacc cacacaccac accacacacc acaccacacc cacacacaca
       61 catcctaaca ctaccctaac acagccctaa tctaaccctg gccaacctgt ctctcaactt
[...]
   230101 tgttagtgtt agtattaggg tgtggtgtgt gggtgtggtg tgggtgtggg tgtgggtgtg
   230161 ggtgtgggtg tgggtgtggt gtggtgtgtg ggtgtggtgt gggtgtggtg tgtgtggg
//
```

On se propose de réaliser un programme `getseqgenbank.py` qui récupère la séquence dans une chaîne de caractères `seq`. Pour cela on utilisera un algorihtme de drapeau ; en pseudo-code, cela donnerait :

```
drapeau <- Faux
seq <- chaîne de caractères vide
Lire toutes les lignes du fichier:
	si la ligne contient //:
	    drapeau <- Faux
	si drapeau est Vrai:
	    on ajoute à seq la ligne (en retirant les espaces, chiffres et retour à la ligne)
	si la ligne contient ORIGIN
	    drapeau <- Vrai
```

Le code affichera :

```
NC_001133.gbk
La séquence fait XXX nucléotides
10 premiers nucléotides: YYYYYYYYYY
10 derniers nucléotides: YYYYYYYYYY
```

où XXX et ZZZ sont des entiers et YYYYYYYYYY sont des nucléotides.
