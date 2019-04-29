# Dictionnaire Correspondance Nucléotides (en majuscule car constante)
NUCLEOTIDES_COMPL = {"A" : "T", "T" : "A", "G" : "C", "C" : "G"}

# Ouverture Lecture Fichier multiFASTA
with open('S_cerevisiae_chromosomes.fna', 'r') as filin:
    chromosome = {}
    # Dictionnaire - Stockage Séquences chromosomiques
    # Parcours Fichier multiFASTA
    for line in filin:
        # Ligne Identifiant FASTA
        if line[0] == '>':
            # Conservation "BK*" uniquement
            ids = line.strip().split(' ')
            id = ids[0].lstrip('>')
            # Création Clé Dictionnaire
            chromosome[id] = ''
            # Ligne Séquence FASTA
        else:
            # Ajout Séquence Majuscule Dictionnaire
            chromosome[id] += line.strip().upper()

# Ouverture Lecture Fichier GFF
with open('S_cerevisiae_annotations.gff', 'r') as filin:
    # Dictionnaire - Stockage CDS
    features = {}
    # Parcours Fichier GFF
    for line in filin:
        # Nettoyage retour à la ligne puis split() sur les tabulations
        champs = line.strip().split("\t")
        # On évite les lignes de commentaire et on ne traite que les CDS
        if len(champs) == 9 and champs[2] == 'CDS':
            # Colonne Attributs
            attributs = champs[8].split(";")
            cds = attributs[0].split("=")[1]
            # Attention ! Les listes Python commence à 0 !
            start = int(champs[3])-1
            # Attention ! Dans les tranches, le 2ème élément n'est pas inclus !
            stop = int(champs[4])
            # Récupération Séquences dans Dictionnaire
            sequence = chromosome[champs[0]][start:stop]
            # Si Brin -
            if champs[6] == '-':
                seq_tmp = ''
                # Parcours de la séquence
                for base in sequence:
                    # on construit le brin complémentaire
                    seq_tmp += NUCLEOTIDES_COMPL[base]
                # puis on l'inverse
                sequence = seq_tmp[::-1]
            # Stockage CDS dans Dictionnaire
            features[cds] = sequence
                        
# Ouverture Ecriture Fichier multiFASTA
with open('S_cerevisiae_cds.fasta', 'w') as filout:
    # Parcours Dictionnaire CDS
    for cds in features.keys():
        # Ecriture Identifiant
        filout.write(">"+cds+"\n")
        # Ecriture Séquence avec découpage par 60
        for n in range(0, len(features[cds]), 60):
            filout.write(features[cds][n:n+60]+"\n")
