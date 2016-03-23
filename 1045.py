n1, n2, n3 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

if (n1 >= n2 and n1 >= n3):
    a = n1
    if (n2 >= n3):
        b = n2
        c = n3
    else:
        b = n3
        c = n2
elif (n2 >= n1 and n2 >= n3):
    a = n2
    if (n1 >= n3):
        b = n1
        c = n3
    else:
        b = n3
        c = n1
elif (n3 >= n1 and n3 >= n2):
    a = n3
    if (n1 >= n2):
        b = n1
        c = n2
    else:
        b = n2
        c = n1

if (a >= (b + c)):
    print("NAO FORMA TRIANGULO")
else:
    if (a * a == b * b + c * c):
        print("TRIANGULO RETANGULO")
    if (a * a > b * b + c * c):
        print("TRIANGULO OBTUSANGULO")
    if (a * a < b * b + c * c):
        print("TRIANGULO ACUTANGULO")
    if (a == b and b == c and c == a):
        print("TRIANGULO EQUILATERO")
    if (a == b) and (b != c) and (c != a):
        print("TRIANGULO ISOSCELES")
    elif (b == c) and (c != a) and (b != a):
        print("TRIANGULO ISOSCELES")
    elif(c == a) and (a != b) and (b != c):
        print("TRIANGULO ISOSCELES")
