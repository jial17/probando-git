altura = 0

n_bloques= int(input("ingrese el numero de bloques: "))
print("numero de bloques:", n_bloques)

while altura < n_bloques:
    altura +=1
    n_bloques-= altura

print("altura: ",altura)
print("bloques restantes: ",n_bloques)