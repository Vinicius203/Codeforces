#include <stdio.h>
#include <stdlib.h>

int main()
{
    int numero, qtd_operacoes, resultado_final;

    scanf("%d %d", &numero, &qtd_operacoes);

    resultado_final = numero;

    for (int operacao = 0; operacao < qtd_operacoes; operacao++)
    {
        if (resultado_final % 10 == 0)
        {
            resultado_final /= 10;
        }
        else
        {
            resultado_final--;
        }
    }

    printf("%d\n", resultado_final);

    return 0;
}