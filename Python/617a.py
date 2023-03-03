posicao_casa = int(input())
posicao_elefante = 0
contador_passos = 0
tamanho_passo = 5

while (posicao_casa > posicao_elefante):
    if(posicao_casa - posicao_elefante >= tamanho_passo):
        posicao_elefante += tamanho_passo
        contador_passos += 1
    else:
        tamanho_passo -= 1
    

print(contador_passos)
