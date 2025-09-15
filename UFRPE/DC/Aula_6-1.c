#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main(void) {
  int amarelo = 0;
  int vermelho = 1;
  int roxo = 2;
  int preto = 3;

  int qtd_amarelo = 0;
  int qtd_vermelho = 0;
  int qtd_roxo = 0;
  int qtd_preto = 0;

  int tam = 10;
  char tabuleiro[tam][tam];

  srand(time(NULL));

  for (int i = 0; i < tam; i++) {
    for (int j = 0; j < tam; j++) {
      tabuleiro[i][j] = rand() % 4;

      switch (tabuleiro[i][j]) {
      case 0:
        qtd_amarelo++;
        break;
      case 1:
        qtd_vermelho++;
        break;
      case 2:
        qtd_roxo++;
        break;
      case 3:
        qtd_preto++;
        break;
      }

      printf("%i ", tabuleiro[i][j]);
    }
    printf("\n");
  }

  printf("\nContagem: \nAmarelos: %i\nVermelhos: %i\nRoxos: %i\nPretos: %i",
         qtd_amarelo, qtd_vermelho, qtd_roxo, qtd_preto);
}
