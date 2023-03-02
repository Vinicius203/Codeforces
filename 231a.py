num_cases = int(input())
a = []

for linhas in range(0, num_cases):
    a.append(input())

exerciciosConcordados = 0

for linhas in a:
    linhaCounter = 0
    for digito in linhas:
        if (digito == '1'):
            linhaCounter += 1

    if linhaCounter >= 2:
        exerciciosConcordados += 1

print(exerciciosConcordados)
