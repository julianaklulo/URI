n = []
pares = 0

for i in range(0, 5):
    n.append(int(input()))
    if (n[i] % 2 == 0):
        pares += 1

print("%d valores pares" % pares)