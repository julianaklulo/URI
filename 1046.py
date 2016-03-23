inicio, fim = input().split()

inicio = int(inicio)
fim = int(fim)

if (fim > inicio):
    print("O JOGO DUROU %d HORA(S)" % (fim - inicio))
else:
    print("O JOGO DUROU %d HORA(S)" % (24 - inicio + fim))
