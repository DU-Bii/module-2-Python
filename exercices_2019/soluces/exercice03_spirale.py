filename="spirale.dat"
x=[]
y=[]
with open(filename, "r") as filin:
    for line in filin:
        coords=line.split()
        # On n'oublie pas de transformer en float les valeurs lues dans le fichier
        x.append(float(coords[0]))
        y.append(float(coords[1]))

print("Nombre de points {}".format(len(x)))
mean=sum(y)/len(y)
print("La moyenne de y est {:.2f}".format(mean))
