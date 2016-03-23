cod1, n1, valor1 = input().split()
cod2, n2, valor2 = input().split()


cod1 = int(cod1)
n1 = int(n1)
valor1 = float(valor1)

cod2 = int(cod2)
n2 = int(n2)
valor2 = float(valor2)

valor_total = ((n1 * valor1) + (n2 * valor2))

print("VALOR A PAGAR: R$ %.2f" % valor_total)
