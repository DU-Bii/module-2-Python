# Ouverture en écriture du fichier tabulé final
with open("B_subtilis_GeneOnly.txt", "w") as filout:
    # Ecriture de l'en-tête du fichier de sortie
    filout.write("{:<12}{:<15}{:<10}{:<10}\n".format("Name","Locus-tag","Start","Stop"))
    # Ouverture en lecture du fichier GFF3 initial
    with open("Bacillus_subtilis.gff3", "r") as filin:
        # Parcours du contenu du fichier ligne par ligne
        for line in filin:
            # Retrait du saut de ligne
            line = line.strip()
            # Si la ligne ne commence pas par un #
            if line[0] != "#":
                # Split sur les tabulations
                champs = line.split("\t")
                # Si la ligne correspond à un gene
                if champs[2] == "gene":
                    start =champs[3]
                    stop = champs[4]
                    # Split de la dernière colonne
                    attributs = champs[8].split(";")
                    # Parcours des différents attributs de la dernière colonne
                    for attribut in attributs:
                        # Solution 1 (avec un split)
                        couple = attribut.split("=")
                        if couple[0] == "gene":
                            gene = couple[1]
                        elif couple[0] == "locus_tag":
                            locustag = couple[1]
                            
                    # Ecriture dans le fichier de sortie
                    filout.write("{:<12}{:<15}{:<10}{:<10}\n".format(gene,locustag,start,stop))
