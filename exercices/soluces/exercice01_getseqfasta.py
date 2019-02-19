filename = "UBI4_SCerevisiae.fasta"
seq = ""
with open(filename, "r") as filin:
    for line in filin:
        if line[0] != '>':
            seq += line.strip()

print(filename)
print("La séquence fait {} nucléotides".format(len(seq)))
if len(seq) % 3 == 0:
    print("La séquence est bien un multiple de 3 nucléotides")
else:
    print("La séquence n'est pas un multiple de 3 nucléotides")
print("La séquence possède {:.0f} codons".format(len(seq)/3))
print("10 premiers nucléotides: {}".format(seq[0:10]))
print("10 derniers nucléotides: {}".format(seq[-10:]))
