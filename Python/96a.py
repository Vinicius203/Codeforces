sequencia = input()
contador_perigo = 0

for bit in range(0, len(sequencia)-1):
    if sequencia[bit] == sequencia[bit+1]:
        contador_perigo += 1
        if (contador_perigo == 6):
            break
    else:
        contador_perigo = 0

if contador_perigo == 6:
    print('YES')
else:
    print('NO')