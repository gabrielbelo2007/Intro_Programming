#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>  

void main()
{
  srand(time(NULL));

  const int tam = 10;
  
  int vetor_pares[tam];
  int vetor_impares[tam];
  int vetor_restantes[tam+tam];

  int indiceV3 = 0;

  for (int i = 0; i < tam; i++){
    vetor_pares[i] = rand() % 10;
    vetor_impares[i] = rand() % 10;
  }

  for (int i= 0; i < tam; i++)
  {
    if (vetor_pares[i] % 2 != 0)
    {
      vetor_restantes[indiceV3] = vetor_pares[i];
      vetor_pares[i] = 0;
      indiceV3++;
    }

    if (vetor_impares[i] % 2 == 0)
    {
      vetor_restantes[indiceV3] = vetor_impares[i];
      vetor_impares[i] = 0;
      indiceV3++;
    }
  }

  for (int num = 0; num < tam; num++)
  {
    printf("%d", vetor_pares[num]);
  }

  printf("\n");

  for (int num = 0; num < tam; num++)
  {
    printf("%d", vetor_impares[num]);
  }

  printf("\n");

  for (int num = 0; num < indiceV3; num++)
  {
    printf("%d", vetor_restantes[num]);
  }
}