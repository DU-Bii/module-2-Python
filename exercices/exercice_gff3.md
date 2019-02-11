## Enoncé de l'exercice GFF3

Le fichier **Bacillus_subtilis.gff3** contient une partie de l'annotation de *Bacillus subtilis* au format GFF3 téléchargé sur RefSeq NCBI. 

```
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
#!genome-build ASM904v1
#!genome-build-accession NCBI_Assembly:GCF_000009045.1
##sequence-region NC_000964.3 1 4215606
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=224308
NC_000964.3	RefSeq	region	1	4215606	.	+	.	ID=id0;Dbxref=taxon:224308;Is_circular=true;gbkey=Src;genome=genomic;mol_type=genomic DNA;strain=168;sub-species=subtilis
NC_000964.3	RefSeq	gene	410	1750	.	+	.	ID=gene0;Name=dnaA;gbkey=Gene;gene=dnaA;gene_biotype=protein_coding;locus_tag=BSU_00010;old_locus_tag=BSU00010
...
```

**Seuls les gènes** (3e colonne = gene) nous intéressent dans cet exercice.

L'objectif final est d'extraire uniquement certaines informations de ces gènes :

* la **position de départ** du gène sur le chromosome (4e colonne),
* la **position de fin** du gène sur le chromosome (5e colonne),
* le **nom** du gène (la sous-partie "Name=" de la 9e colonne),
* le ***locus_tag*** associé au gène (la sous-partie "locus_tag=" de la 9e colonne).

Vous pouvez écrire vos données dans un fichier tabulé sous la forme :

```
Name  Locus-tag Start Stop
dnaA  BSU_00010 410 1750
```
