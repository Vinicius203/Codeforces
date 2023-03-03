operacoes = int(input())
contador = 0

for i in range(0, operacoes):
    operacao = input()
    if '+' in operacao:
        contador += 1
    else:
        contador -= 1

print(contador)
