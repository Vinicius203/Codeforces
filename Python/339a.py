def insereAdicao(operacao):
    i = 0
    operacao_final = ''
    operacao_final += operacao[0]
    for i in range(1, len(operacao)):
        operacao_final += ('+' + operacao[i])

    return operacao_final


operacao_impossivel = input()

operacao_possivel = operacao_impossivel.replace("+", "")
operacao_possivel = sorted(operacao_possivel)

print(insereAdicao(operacao_possivel))
