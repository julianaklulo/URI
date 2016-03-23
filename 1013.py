a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maiorab = (a + b + abs(a - b)) / 2
maiorabc = (maiorab + c + abs(maiorab - c)) / 2

print("%d eh o maior" % maiorabc)
