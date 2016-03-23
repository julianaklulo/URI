n = int(input())
numbers = []

intervalo = 0

for i in range(0, n):
    numbers.append(int(input()))
    if (numbers[i] >= 10 and numbers[i] <= 20):
        intervalo += 1

print("%d in" % intervalo)
print("%d out" % (n - intervalo))
