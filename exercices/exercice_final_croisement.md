## Enoncé de l'exercice sur le croisement de données

Le fichier [S_cerevisiae_chromosomes.fna](http://www.dsimb.inserm.fr/~fuchs/DUBii/S_cerevisiae_chromosomes.fna) contient les 16 **séquences chromosomiques** de la levure *Saccharomyces cerevisiae*.

```
>BK006935.2 TPA_inf: Saccharomyces cerevisiae S288c chromosome I, complete sequence
ccacaccacacccacacacccacacaccacaccacacaccacaccacacccacacacacacatCCTAACACTACCCTAAC
ACAGCCCTAATCTAACCCTGGCCAACCTGTCTCTCAACTTACCCTCCATTACCCTGCCTCCACTCGTTACCCTGTCCCAT
TCAACCATACCACTCCGAACCACCATCCATCCCTCTACTTACTACCACTCACCCACCGTTACCCTCCAATTACCCATATC
...
```

Le fichier [S_cerevisiae_annotations.gff](http://www.dsimb.inserm.fr/~fuchs/DUBii/S_cerevisiae_annotations.gff) contient l’**annotation** du génome de la levure *Saccharomyces cerevisiae*.

```
##gff-version 3
#!gff-spec-version 1.20
#!processor NCBI annotwriter
#!genome-build R64-1-1
#!genome-build-accession NCBI_Assembly:GCA_000146045.2
##sequence-region BK006935.2 1 230218
##species http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=559292
BK006935.2	tpg	region	1	230218	.	+	.	ID=id0;Dbxref=taxon:559292;Name=I;chromosome=I;gbkey=Src;genome=chromosome;mol_type=genomic DNA;strain=S288c
BK006935.2	tpg	region	1	801	.	-	.	ID=id1;Dbxref=SGD:S000028862;Note=TEL01L%3B Telomeric region on the left arm of Chromosome I%3B composed of an X element core sequence%2C X element combinatorial repeats%2C and a short terminal stretch of telomeric repeats;gbkey=telomere
BK006935.2	tpg	gene	1807	2169	.	-	.	ID=gene0;Name=PAU8;gbkey=Gene;gene=PAU8;locus_tag=YAL068C
BK006935.2	tpg	mRNA	1807	2169	.	-	.	ID=rna0;Parent=gene0;gbkey=mRNA;gene=PAU8;product=seripauperin PAU8
BK006935.2	tpg	exon	1807	2169	.	-	.	ID=id3;Parent=rna0;gbkey=mRNA;gene=PAU8;product=seripauperin PAU8
BK006935.2	tpg	CDS	1807	2169	.	-	0	ID=cds0;Parent=rna0;Dbxref=SGD:S000002142,NCBI_GP:DAA06918.1;Name=DAA06918.1;Note=hypothetical protein%3B member of the seripauperin multigene family encoded mainly in subtelomeric regions;gbkey=CDS;gene=PAU8;product=seripauperin PAU8;protein_id=DAA06918.1
...
```

L'objectif de cet exercice est de créer un **fichier multi-FASTA** contenant les **séquences** des **CDS** annotées (3e colonne contient "CDS").

Vous trouverez le **nom de la séquence de référence** (1e colonne), les **positions de début** (4e colonne) et **de fin** (5e colonne), le **sens** de la séquence (7e colonne) ainsi que l'**identifiant** associé à la séquence codante (sous-partie "ID=" de la 9e colonne) dans le fichier d'annotation.
Vous pourrez ainsi récupérer la portion de séquence d'intérêt dans le fichier multiFASTA.

**Exemple de sortie :**

```
>cds0
ATGGTCAAATTAACTTCAATCGCCGCTGGTGTCGCTGCCATCGCTGCTACTGCTTCTGCA
ACCACCACTCTAGCTCAATCTGACGAAAGAGTCAACTTGGTGGAATTGGGTGTCTACGTC
TCTGATATCAGAGCTCACTTAGCCCAATACTACATGTTCCAAGCCGCCCACCCAACTGAA
ACCTACCCAGTCGAAGTTGCTGAAGCCGTTTTCAACTACGGTGACTTCACCACCATGTTG
ACCGGTATTGCTCCAGACCAAGTGACCAGAATGATCACCGGTGTTCCATGGTACTCCAGC
AGATTAAAGCCAGCCATCTCCAGTGCTCTATCCAAGGACGGTATCTACACTATCGCAAAC
TAG
```

*Remarques :*

* le format multiFASTA impose que la séquence soit découpée (60 caractères par ligne).
* les séquences doivent être en lettres majuscules uniquement.

Si vous avez les idées claires sur ce qu'il faut faire, vous pouvez arrêter votre lecture ici et vous lancer. Si ce n'est pas le cas et que vous ne savez pas par où commencer, voici quelques pistes :

**Traitement du fichier multiFASTA**

* parcours en lecture du fichier **S_cerevisiae_chromosomes.fna**,
* création d'un dictionnaire (**clé** : nom de la séquence chromosomique , **valeur** : séquence chromosomique).

*Point d'attention : dans un fichier au format FASTA, la séquence peut être sur plusieurs lignes.* 

**Traitement du fichier GFF3**

* parcours en lecture du fichier **S_cerevisiae_annotations.gff**,
* filtrage sur le type de *feature* (la 3e colonne doit contenir **CDS**),
* récupération des éléments d'intérêt (**nom de la séquence de référence** dans la 1e colonne, les **positions de début** et **de fin** respectivement dans les 4e colonne et 5e colonne, le **sens** de la séquence dans la 7e colonne ainsi que l'**identifiant** associé à la séquence codante qui correspondant à la sous-partie "ID=" de la 9e colonne).

**Croisement des données**

* grâce aux positions de début et de fin du *feature* de type CDS, vous pouvez **extraire sa séquence** à partir du dictionnaire préalablement créé,
* dans le cas où l'élement est positionné sur le **brin -**, il faudra **"inverse complémenter"** la séquence :

```
séquence initiale :               5'-ATGC-3'
séquence complémentaire :         3'-TACG-5'
séquence inverse complémentaire : 5'-GCAT-3'
```
