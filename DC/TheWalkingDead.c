#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main(void) {
  srand(time(NULL));
  int tam = 25;
  char mapa[tam][tam+1];

  for(int i = 0; i < tam; i++){
    for(int j= 0; j < tam; j++){
      mapa[i][j] = ' ';
      printf("%c ", mapa[i][j]);
    }
    printf("\n");
  }

  int rick = 1;
  int zumbis = 10;
  int balas = 10;
  int obstaculos = 20;
  int saida = 1;
  
  int x_r = rand() % tam;
  int y_r = rand() % tam;
  mapa[x_r][y_r] = 'R';

  for()
  
  for(int i = 0; i < tam; i++){
    for(int j= 0; j < tam; j++){
      printf("%c ", mapa[i][j]);
    }
    printf("\n");
  }
}
