# Ouverture en lecture du fichier CSV initial
with open("Truite_ChrName_RefSeq.csv", "r") as filin:
    # Initialisation d'un dictionnaire
    dico = {}
    # Parcours du fichier ligne par ligne
    for line in filin:
        # Si la ligne commence par "chr"
        if line.startswith("Chr") == True:
            # On nettoie le retour à la ligne avec strip() puis
            # split() sur le séparateur de colonnes ";"
            colonnes = line.strip().split(";")
            # recup du numéro de chromosome
            num_chrom = int(colonnes[1])
            # construction clé (par exemple "Chr01")
            name = "{}{:02d}".format(colonnes[0], num_chrom)
            # Remplissage du dictionnaire (clé = Chr* ; valeur = Référence RefSeq)
            dico[name] = colonnes[2]
        
# Parcours du dictionnaire   
for chrom in dico:
    print("{} ::: {}".format(chrom, dico[chrom]))
