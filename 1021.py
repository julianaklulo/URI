n = float(input())

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

resto = resto % 1

moeda_50 = resto / 0.50

resto = resto - (moeda_50 * 0.50)

moeda_25 = resto / 0.25

resto = resto - (moeda_25 * 0.25)

moeda_10 = resto / 0.10

resto = resto - (moeda_10 * 0.10)

moeda_5 = resto / 0.05

resto = resto - (moeda_5 * 0.05)

moeda_1 = resto / 0.01

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % cem)
print("%d nota(s) de R$ 50.00" % cinquenta)
print("%d nota(s) de R$ 20.00" % vinte)
print("%d nota(s) de R$ 10.00" % dez)
print("%d nota(s) de R$ 5.00" % cinco)
print("%d nota(s) de R$ 2.00" % dois)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % um)
print("%d moeda(s) de R$ 0.50" % moeda_50)
print("%d moeda(s) de R$ 0.25" % moeda_25)
print("%d moeda(s) de R$ 0.10" % moeda_10)
print("%d moeda(s) de R$ 0.05" % moeda_5)
print("%d moeda(s) de R$ 0.01" % moeda_1)
