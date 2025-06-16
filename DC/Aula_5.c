#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>  

void main(){
  srand(time(NULL));

  int tam = 10; 
  
  int vetor_pares[tam];
  int vetor_impares[tam];
  int vetor_restantes[tam+tam];

  for (int i = 0; i < tam; i++){
    vetor_pares[i] = rand() % 10;
    vetor_impares[i] = rand() % 10;
  }
