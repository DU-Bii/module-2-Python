# Dictionnaire correspondance nucléotides (en majuscule car constante).
NUCLEOTIDES_COMPL = {"A" : "T", "T" : "A", "G" : "C", "C" : "G"}

# Lecture des séquences du fichier multiFASTA.
with open('S_cerevisiae_chromosomes.fna', 'r') as filin:
    # Dictionnaire - stockage séquences chromosomiques.
    chromosome = {}
    # Parcours fichier multiFASTA.
    for line in filin:
        # Ligne identifiant FASTA.
        if line.startswith('>'):
            # Conservation "BK*" uniquement.
            split_comment_line = line.strip().split(' ')
            chr_id = split_comment_line[0].lstrip('>')
            # Création clé dictionnaire.
            chromosome[chr_id] = ''
        else:
            # Ligne séquence FASTA, ajout séquence majuscule ds dictionnaire.
            chromosome[chr_id] += line.strip().upper()

# Ouverture lecture fichier GFF (https://fr.wikipedia.org/wiki/General_feature_format)
# et du fichier de sortie multiFASTA.
with open('S_cerevisiae_annotations.gff', 'r') as filin, \
     open('S_cerevisiae_cds.fasta', 'w') as filout:
    # Parcours fichier GFF.
    for line in filin:
        # Nettoyage retour à la ligne puis split() sur les tabulations.
        champs = line.strip().split("\t")
        # On évite les lignes de commentaire et on ne traite que les CDS.
        if not line.startswith("#") and champs[2] == 'CDS':
            # id du chromosome.
            chr_id = champs[0]
            # Attention, les listes Python commence à 0 !
            debut = int(champs[3]) - 1
            # Attention, dans les tranches, le 2ème élément n'est pas inclus !
            fin = int(champs[4])
            # Sens du brin.
            brin = champs[6]
            # Récupération de l'id de la CDS.
            attributs = champs[8].split(";")
            id_cds = attributs[0].split("=")[1]
            # Récupération de la séquence.
            sequence = chromosome[chr_id][debut:fin]
            # Traitement brin complémentaire.
            if brin == '-':
                seq_tmp = ''
                # Parcours de la séquence.
                for base in sequence:
                    # On construit le brin complémentaire.
                    seq_tmp += NUCLEOTIDES_COMPL[base]
                # Puis on l'inverse.
                sequence = seq_tmp[::-1]
            # Ecriture identifiant dans le fichier de sortie.
            filout.write("> {}\n".format(id_cds))
            # Ecriture séquence (60 nucléotides par ligne).
            for n in range(0, len(sequence), 60):
                filout.write("{}\n".format(sequence[n:n+60]))
