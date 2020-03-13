N = int(input("Entrez un nb de lignes: "))
for i in range(1, N+1):
    nb_spc = N - i
    nb_star = 2*i - 1
    print(" "*nb_spc + "*"*nb_star)
 
