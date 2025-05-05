#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void){

// Operadores matemáticos (math.h)
  float num1, num2;
  printf("Escreva dois números: ");
  scanf("%f %f", &num1, &num2);

  float raizSen = sqrt(sin(num1));
  float elevadoCos = pow(num1, cos(num2));

  printf("O resultado da raiz do seno do número %f é: %f", num1, raizSen);

  printf("O resultado do número %f elevado ao cosseno do número %f é: %f", num1, num2,
         elevadoCos);

  
// Números aleatórios 
    srand(time(NULL));
        
    int num3 = 50 + rand() % 151;  // random entre 50 e 200
        
    if(num3 % 2 == 0){
        printf("O número %i é par", num3);
    } else {
        printf("O número %i é ímpar", num3);
    }; 


// Condicional composta

    int num4 = rand() % 101; 

    if(num4 > 50){
        printf("O número %i é maior que 50", num4);
    } else if (num4 == 50) {
        printf("O número %i é igual a 50", num4);
    } else {
        printf("O número %i é menor que 50", num4);
    };
    
    return 0;

}