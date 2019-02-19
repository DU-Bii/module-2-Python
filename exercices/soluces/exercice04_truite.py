# Ouverture en lecture du fichier CSV initial
with open("Truite_ChrName_RefSeq.csv", "r") as filin:
    # Initialisation d'un dictionnaire
    dico = {}
    # Parcours du fichier ligne par ligne
    for line in filin:
        # Retrait du saut de ligne
        line = line.strip()
        # Si la ligne commence par "chr"
        if line.startswith("Chr") == True:
            # Split sur le séparateur de colonnes ";"
            colonnes = line.split(";")
            # Si le numéro du chromosome est un chiffre alors on ajoute un 0 entre "chr" et le numéro
            if len(colonnes[1]) == 1:
                name = colonnes[0]+"0"+colonnes[1]
            # Sinon pas besoin
            else:
                name = colonnes[0]+colonnes[1]
            # Remplissage du dictionnaire (clé = Chr* ; valeur = Référence RefSeq)
            dico[name] = colonnes[2]
        
# Parcours du dictionnaire   
for chr in dico:
    print("{} ::: {}".format(chr, dico[chr]))
