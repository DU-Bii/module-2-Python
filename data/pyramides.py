N = int(input("Entrez un nb d'étoiles: "))
for i in range(1, N+1, 2):
    print("{:^{}s}".format("*"*i, N))
