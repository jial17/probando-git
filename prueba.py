altura = 0
requeridos= 0


n_bloques= int(input("ingrese el numero de bloques: "))
print("numero de bloques", n_bloques)

while requeridos < n_bloques:
    altura +=1
    requeridos = altura
    n_bloques-= altura

print("altura",altura)