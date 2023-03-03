participantes, corte = input().split()

participantes_int = int(participantes)
corte_int = int(corte)

notas = []

notas.append(input().split())

contaAprovados = 0

for lista in notas:
    for valor in lista:
        if (int(valor) >= int(lista[corte_int-1]) and int(valor) != 0):
            contaAprovados += 1

print(contaAprovados)
