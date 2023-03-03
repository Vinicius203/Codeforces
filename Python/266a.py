num_stones = int(input())
cores = input()


def verificaVizinho(cores):
    contador = 0
    for cor in range(0, len(cores)-1):
        if cores[cor] != cores[cor+1]:
            contador += 1

    return contador


def transforma(cores):
    nova_sequencia = []
    nova_sequencia.append(cores[0])
    j = 0
    for cor in range(0, len(cores)):
        if (cores[cor] != nova_sequencia[j]):
            nova_sequencia.append(cores[cor])
            j += 1

    return nova_sequencia


verifica = verificaVizinho(cores)

if verifica == (len(cores)-1):
    print('0')
else:
    novo_tamanho = transforma(cores)
    resultado_movimentos = len(cores) - len(novo_tamanho)
    print(resultado_movimentos)
