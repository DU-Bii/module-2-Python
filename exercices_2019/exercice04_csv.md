# Exercice 04 truite et csv

Le fichier [Truite_ChrName_RefSeq.csv](Truite_ChrName_RefSeq.csv) contient diverses informations sur l’annotation du génome de la truite Arc-en-ciel.

```
Type;Name;RefSeq;Size (Mb);GC%;Protein;rRNA;tRNA;Other RNA;Gene;Pseudogene
Chr;1;NC_035077.1;84.88;43.0;2,679;-;12;261;1,679;76
Chr;2;NC_035078.1;85.48;43.1;3,229;-;50;304;2,153;75
Chr;3;NC_035079.1;84.94;43.5;3,193;-;15;323;2,179;95
...
```

Vous y trouverez une ligne par chromosome avec les informations suivantes :
* numéro du chromosome,
* référence RefSeq,
* taille,
* pourcentage de GC,
* nombre de protéines, de gènes, de pseudogènes et d’ARNs.

L’information qui nous intéresse est la **correspondance** entre le **numéro de chaque chromosome** et la **référence RefSeq** 
(exemples : Chr01 <—> NC_035077, Chr02 <-> NC_035078.1, ..., Chr10 <—> NC_035086.1, ...).

Créez un programme `truite.py` qui va lire le fichier csv, extraire les informations idoines, et stocker la correspondance numéro/nom de chromosome <-> refseq sous forme d’un **dictionnaire**. Par exemple pour le chromosome 1, la clé sera `Chr01` et la valeur `NC_035077`. Ce dictionnaire sera affiché à l'écran par votre programme.
