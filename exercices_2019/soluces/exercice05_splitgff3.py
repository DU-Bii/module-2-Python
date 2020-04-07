# Ouverture en lecture du fichier GFF3 initial
# Ouverture en écriture du fichier tabulé final
with open("Bacillus_subtilis.gff3", "r") as filin, \
     open("B_subtilis_GeneOnly.txt", "w") as filout:
    # Ecriture de l'en-tête du fichier de sortie
    filout.write("{:<12}{:<15}{:<10}{:<10}\n".format("Name","Locus-tag",
                                                     "Start","Stop"))
    # Parcours du contenu du fichier ligne par ligne
    for line in filin:
        # Si la ligne ne commence pas par un #
        if not(line.startswith("#")):
            # On nettoie le retour à la ligne avec strip() puis
            # split() sur les tabulations
            champs = line.strip().split("\t")
            # Si la ligne correspond à un gene
            if champs[2] == "gene":
                start = int(champs[3])
                stop = int(champs[4])
                # split() de la dernière colonne sur le point-virgule
                attributs = champs[8].split(";")
                # Parcours des différents attributs de la dernière colonne
                for attribut in attributs:
                    # Split sur le caractère "="
                    couple = attribut.split("=")
                    if couple[0] == "gene":
                        gene = couple[1]
                    elif couple[0] == "locus_tag":
                        locustag = couple[1]
                # Ecriture dans le fichier de sortie
                filout.write("{:<12s}{:<15s}{:<10d}{:<10d}\n"
                             .format(gene, locustag, start, stop))
