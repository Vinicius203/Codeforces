#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int contaMovimentos(int index);

int main()
{
    int matriz[5][5], index_linha, index_coluna, contador_movimentos = 0;

    for (int linha = 0; linha < 5; linha++)
    {
        for (int coluna = 0; coluna < 5; coluna++)
        {
            scanf("%d", &matriz[linha][coluna]);
        }
    }

    for (int linha = 0; linha < 5; linha++)
    {
        for (int coluna = 0; coluna < 5; coluna++)
        {
            if (matriz[linha][coluna] == 1)
            {
                index_linha = linha;
                index_coluna = coluna;
            }
        }
    }

    contador_movimentos = contaMovimentos(index_linha) + contaMovimentos(index_coluna);
    printf("%d\n", contador_movimentos);

    return 0;
}

int contaMovimentos(int index)
{
    int qtd_movimentos = 0;

    if (index == 2)
    {
        return 0;
    }

    else
    {
        qtd_movimentos = abs(2 - index);
    }

    return qtd_movimentos;
}