
#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#include "math.h"

void main()
{

    //  1

    // int total;
    // int pagas;
    // int valor;
    //
    // printf("Digite o total de prestações, quantas foram pagas e o valor de cada uma: ");
    // scanf("%i %i %i", &total, &pagas, &valor);
    //
    // int saldo = total * valor - pagas * valor;
    // int restantes = total - pagas;
    // printf("O saldo devedor: %.2i faltam %i prestações", saldo, restantes);

    // 2

    srand(time(NULL));

    int a, b, c;
    a = 1 + rand() % 20;
    b = 1 + rand() % 20;
    c = 1 + rand() % 20;

    printf("%i %i %i", a, b, c);

    float result = (-b + sqrt(pow(b, 2) + 4*a*c)) / (2*a);
    printf("O resultado eh: %f", result);

    return 0;
}
