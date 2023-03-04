#include <stdio.h>
#include <stdlib.h>

int totalSum(int numberCoins, int *values);
int coinsNeeded(int numberCoins, int *values);
void bubblesort(int numberCoins, int *values);
void swap(int *values, int i, int j);

int main()
{
    int numberCoins, num_coins;

    scanf("%d", &numberCoins);

    int values[numberCoins];

    for (int valor = 0; valor < numberCoins; valor++)
    {
        scanf("%d", &values[valor]);
    }

    num_coins = coinsNeeded(numberCoins, values);
    printf("%d", num_coins);
}

int totalSum(int numberCoins, int *values)
{
    int total = 0;
    for (int i = 0; i < numberCoins; i++)
    {
        total += *(values + i);
    }

    return total;
}

void swap(int *values, int i, int j)
{
    int aux;
    aux = values[i];
    values[i] = values[j];
    values[j] = aux;
}

void bubblesort(int numberCoins, int *values)
{
    for (int i = 0; i < numberCoins - 1; i++)
    {
        for (int j = numberCoins - 1; j > i; j--)
        {
            if (values[j] < values[j - 1])
                swap(values, j, j - 1);
        }
    }
}

int coinsNeeded(int numberCoins, int *values)
{
    int neededValue = 0, total = 0, coins_cont = 0;
    total = totalSum(numberCoins, values);

    bubblesort(numberCoins, values);

    for (int i = numberCoins - 1; i >= 0; i--)
    {
        if (neededValue > total)
        {
            break;
        }
        else
        {
            neededValue += *(values + i);
            total -= *(values + i);
            coins_cont++;
        }
    }

    return coins_cont;
}
