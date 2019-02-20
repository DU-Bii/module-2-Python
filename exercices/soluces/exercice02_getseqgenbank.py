filename="NC_001133.gbk"
seq = ""
is_seq = False
with open(filename, "r") as filin:
    for line in filin:
        if line.startswith("//"):
            is_seq = False
        if is_seq:
            seq += line[10:-1].replace(" ", "")
        if line.startswith("ORIGIN"):
            is_seq = True


print(filename)
print("La séquence fait {} nucléotides".format(len(seq)))
print("10 premiers nucléotides: {}".format(seq[0:10]))
print("10 derniers nucléotides: {}".format(seq[-10:]))
