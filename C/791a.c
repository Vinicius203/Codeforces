#include <stdio.h>
#include <stdlib.h>

int main()
{
    int peso_limak, peso_bob, conta_anos = 0;

    scanf("%d %d", &peso_limak, &peso_bob);

    while (peso_limak <= peso_bob)
    {
        peso_limak *= 3;
        peso_bob *= 2;
        conta_anos++;
    }

    printf("%d\n", conta_anos);

    return 0;
}