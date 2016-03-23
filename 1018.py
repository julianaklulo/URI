n = int(input())

cem = n / 100

resto = n % 100

cinquenta = resto / 50

resto = resto % 50

vinte = resto / 20

resto = resto % 20

dez = resto / 10

resto = resto % 10

cinco = resto / 5

resto = resto % 5

dois = resto / 2

resto = resto % 2

um = resto / 1

print(n)
print("%d nota(s) de R$ 100,00" % cem)
print("%d nota(s) de R$ 50,00" % cinquenta)
print("%d nota(s) de R$ 20,00" % vinte)
print("%d nota(s) de R$ 10,00" % dez)
print("%d nota(s) de R$ 5,00" % cinco)
print("%d nota(s) de R$ 2,00" % dois)
print("%d nota(s) de R$ 1,00" % um)
