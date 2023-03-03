#include <stdio.h>
#include <stdlib.h>

int main()
{
    int preco_banana, dinheiro, qtd_bananas;

    scanf("%d %d %d", &preco_banana, &dinheiro, &qtd_bananas);

    for (int numero_banana = 1; numero_banana <= qtd_bananas; numero_banana++)
    {
        dinheiro -= numero_banana * preco_banana;
    }

    if (dinheiro < 0)
    {
        printf("%d\n", abs(dinheiro));
    }
    else
    {
        printf("%d\n", 0);
    }

    return 0;
}