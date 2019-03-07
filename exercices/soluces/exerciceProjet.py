# Ouverture Lecture Fichier multiFASTA
with open('S_cerevisiae_chromosomes.fna', 'r') as filin:
        # Dictionnaire - Stockage Séquences chromosomiques
        chromosome = {}
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
                # On évite les lignes de commentaire et on traite que les CDS
                if len(champs) == 9 and champs[2] == 'CDS':
                        # Colonne Attributs
                        attributs = champs[8].split(";")
                        cds = attributs[0].split("=")[1]
                        start = int(champs[3])
                        stop = int(champs[4])
                        # Récupération Séquences dans Dictionnaire
                        sequence = chromosome[champs[0]][start:stop]
                        # Si Brin -
                        if champs[6] == '-':
                                seq = ''
                                # Dictionnaire Correspondance Nucléotides
                                nucleotides = {"A" : "T", "T" : "A", "G" : "C", "C" : "G"}
                                # Parcours de la séquence
                                for i in range(len(sequence)):
                                        # Nucléotide en partant de la fin
                                        nucl = sequence[len(sequence)-1-i]
                                        # Correspondance à partir dictionnaire
                                        seq += nucleotides[nucl]
                                sequence = seq
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
