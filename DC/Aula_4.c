#  include <stdio.h>
#  include <time.h>
#  include <stdlib.h>

// ATIVIDADE - Número da Sorte

// int main(void) {
//   srand(time(NULL));

//   int num_aleatorio = rand() % 101;
//   int palpite;
//   int tentativas = 0;

//   do {
//     do { printf("\nDigite um numero (0 a 100): ");
//        scanf("%i", &palpite);
//        getchar();
//     } while(palpite > 100 || palpite < 0);
    
//     if (palpite > num_aleatorio){
//       tentativas++;
//       printf("O número aleatório é menor que o seu palpite!\nVocê tem %i tentativas", tentativas);
//     } else if (palpite < num_aleatorio) {
//       tentativas++;
//       printf("O número aleatório é maior que o seu palpite!\nVocê tem %i tentativas", tentativas);
//     }
//   } while(palpite != num_aleatorio && tentativas > 0);

//   printf("Você acertou o número!\nO total de tentativas foi: %i", tentativas);
// }

// Laço FOR

// int main(void){
//   for (inicialização ; condição ; incremento)

//   int num_tabuada;
//   printf("Digite um número: ");
//   scanf("%i", &num_tabuada);
//   printf("\nTabuada do número %i\n", num_tabuada);
  
//   for (int x = 1; x <= 10; x++){
//     int resultado = num_tabuada * x;
//     printf("%i * %i = %i\n", num_tabuada, x, resultado);
//   }
  
//   for(int tabuada = 2; tabuada <= 20; tabuada++){
//     printf("\n# Tabuada do %i\n", tabuada);
//     for(int x = 1; x <= 10; x++){
//       int resultado = tabuada * x;
//       printf("%i * %i = %i\n", tabuada, x, resultado);
//     }
//   }
// 

int main(void) {

  int numero;

  printf("Digite um número: ");
  scanf("%i", &numero);

  int n_bolas = 0;
  int n_X = numero;

  for(int l = numero; l >= 0; l--){

    for(int o = 0; o < n_bolas; o++){
      printf("O ");
    }

    for (int x = 0; x < n_X; x++){
      printf("X ");
    }
    printf("\n");

    n_bolas++;
    n_X--;
  }
}



