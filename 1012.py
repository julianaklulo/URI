pi = 3.14159

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

tri = (A * C) / 2
c = pi * (C * C)
tra = ((A + B) * C) / 2
q = B * B
r = A * B

print("TRIANGULO: %.3f" % tri)
print("CIRCULO: %.3f" % c)
print("TRAPEZIO: %.3f" % tra)
print("QUADRADO: %.3f" % q)
print("RETANGULO: %.3f" % r)
