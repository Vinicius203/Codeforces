#include <stdio.h>
#include <stdlib.h>

void isolatedCell(int rows, int columns);

int main()
{
    int num_cases, rows, columns;

    scanf("%d", &num_cases);

    for (int i = 0; i < num_cases; i++)
    {
        scanf("%d %d", &rows, &columns);
        isolatedCell(rows, columns);
    }
}

void isolatedCell(int rows, int columns)
{
    if ((rows >= 4 || columns >= 4) || (rows <= 2 && columns <= 2) || (rows == 1 || columns == 1))
    {
        printf("%d %d\n", rows, columns);
    }
    else
    {
        printf("%d %d\n", 2, 2);
    }
}