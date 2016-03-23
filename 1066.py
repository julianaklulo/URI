n = []
pares = 0
positivos = 0
negativos = 0

for i in range(0, 5):
    n.append(int(input()))
    if (n[i] % 2 == 0 or n[i] == 0):
        pares += 1

    if (n[i] > 0):
        positivos += 1
    elif (n[i] < 0):
        negativos += 1

print("%d valor(es) par(es)" % pares)
print("%d valor(es) impar(es)" % (5 - pares))
print("%d valor(es) positivo(s)" % positivos)
print("%d valor(es) negativo(s)" % negativos)
