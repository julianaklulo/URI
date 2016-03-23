salario = float(input())

if (salario <= 400.00):
    reajuste = 0.15
elif (salario >= 400.01 and salario <= 800):
    reajuste = 0.12
elif (salario >= 800.01 and salario <= 1200.00):
    reajuste = 0.1
elif (salario >= 1200.01 and salario <= 2000.00):
    reajuste = 0.07
elif (salario > 2000):
    reajuste = 0.04

novoSalario = salario + (salario * reajuste)

print("Novo salario: %.2f" % novoSalario)
print("Reajuste ganho: %.2f" % (salario * reajuste))
print("Em percentual: %d " % (reajuste * 100) + "%")
