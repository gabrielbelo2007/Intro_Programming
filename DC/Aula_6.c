#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main(void) {

  srand(time(NULL));
  
  int matriz_1[6][6];
  int matriz_2[6][6];
  int matriz_3[6][5];
  
  for (int i = 0; i < 6; i++){
    for(int j= 0; j < 6; j++){
      
      int valor = rand() % 10;
      matriz_1[i][j] = valor;
      printf("%i ", matriz_1[i][j]);
    }
    printf("\n");
  }

  printf("\n");
  
  for (int i = 0; i < 6; i++){
    for(int j= 0; j < 6; j++){

      int valor = rand() % 10;
      matriz_2[i][j] = valor;
      printf("%i ", matriz_2[i][j]);
    }
    printf("\n");
  } 

  printf("\n");
  
  for (int i = 0; i < 6; i++){
    for(int j = 0; j < 6; j++){
      
      matriz_3[i][j] = (matriz_1[i][j] + matriz_2[i][j]);
      printf("%i ", matriz_3[i][j]);
    }
    printf("\n");
  }
  
}
