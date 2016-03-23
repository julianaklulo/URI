salario = float(input())

if (salario <= 2000.00):
	print ("Isento")
elif (salario >= 2000.01 and salario <= 3000.00):
	print("R$ %.2f" % ((salario - 2000.00) * 0.08))
elif (salario >= 3000.01 and salario <= 4500.00):
	print("R$ %.2f" % ((salario - 2000.00) * 0.18))