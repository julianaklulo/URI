n = int(input())

anos = n / 365

resto = n % 365

meses = resto / 30

resto = resto % 30

dias = resto

print("%d ano(s)" % anos)
print("%d mes(es)" % meses)
print("%d dia(s)" % dias)
