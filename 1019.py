n = int(input())

horas = n / 3600

resto = n % 3600

minutos = resto / 60

resto = resto % 60

segundos = resto

print("%d:%d:%d" % (horas, minutos, segundos))
