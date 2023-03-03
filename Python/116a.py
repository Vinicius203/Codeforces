paradas = int(input())

saida_entrada = []
contador_capacidade = 0
lista_capacidade = []


for i in range(0, paradas):
    saida_entrada.append(input().split())

for movimentos in saida_entrada:
    for i, movimento in enumerate(movimentos):
        if (i == 0):
            contador_capacidade -= int(movimento)
        else:
            contador_capacidade += int(movimento)

    lista_capacidade.append(contador_capacidade)

print(max(lista_capacidade))
