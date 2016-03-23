n = []

positivo = 0
media = 0

for i in range(0, 6):
    n.append(float(input()))

for i in range(0, 6):
    if (n[i] > 0):
        positivo += 1
        media += n[i]

media = media / positivo

print("%d valores positivos" % positivo)
print(media)
