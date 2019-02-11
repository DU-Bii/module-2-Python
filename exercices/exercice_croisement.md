## Enoncé de l'exercice sur le croisement de données

Le fichier **S_cerevisiae_chromosomes.fna** contient les 16 **séquences chromosomiques** de la levure *Saccharomyces cerevisiae*.

```
>BK006935.2 TPA_inf: Saccharomyces cerevisiae S288c chromosome I, complete sequence
ccacaccacacccacacacccacacaccacaccacacaccacaccacacccacacacacacatCCTAACACTACCCTAAC
ACAGCCCTAATCTAACCCTGGCCAACCTGTCTCTCAACTTACCCTCCATTACCCTGCCTCCACTCGTTACCCTGTCCCAT
TCAACCATACCACTCCGAACCACCATCCATCCCTCTACTTACTACCACTCACCCACCGTTACCCTCCAATTACCCATATC
...
```

Le fichier **S_cerevisiae_annotations.gff** contient l’**annotation** du génome de la levure *Saccharomyces cerevisiae*.

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

Les fichiers se trouvent [ici](https://filesender.renater.fr/?s=download&token=ddb647e6-294c-3ce8-5467-bb6c1f927e3a).

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