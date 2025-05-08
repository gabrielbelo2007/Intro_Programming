# include <stdio.h>
# include <math.h>
# include <stdlib.h>

// CALCULADORA

// int main(void) {
//   float num1, num2, resultado;
//   char operador;
//   char sair = 's';
//   printf("Calculdora (Operações: + ; - ; * ; /)\n");

//   while (sair == 's'){
//     printf("\nEscreva uma expressão: ");
//     scanf("%f %c %f", &num1, &operador, &num2);
//     getchar();
  
//     if(operador == '+'){
//       resultado = num1 + num2;
//       printf("%2.f %c %2.f = %2.f", num1, operador, num2, resultado);
//     } else if ( operador == '-') {
//       resultado = num1 - num2;
//       printf("%2.f %c %2.f = %2.f", num1, operador, num2, resultado);
//     } else if (operador == '*') {
//       resultado = num1 * num2;
//       printf("%2.f %c %2.f = %2.f", num1, operador, num2, resultado);
//     } else if (operador == '/') {
//       if(num2 == 0){
//         printf("Não é possível realizar essa operação");
//       } else {
//         resultado = num1 / num2;
//         printf("%2.f %c %2.f = %2.f", num1, operador, num2, resultado);
//       }
//     } else {
//       printf("Selecione um operador válido");
//     }

      // switch(operador){
      //   case "+": printf("%2.f %c %2.f = %2.f", num1, operador, num2, resultado); break;
      //   case "-": printf("%2.f %c %2.f = %2.f", num1, operador, num2, resultado); break;
      //   case "*": printf("%2.f %c %2.f = %2.f", num1, operador, num2, resultado); break;
      //   case "/": if(num2 == 0){
      //           printf("Não é possível realizar essa operação");
      //         } else {
      //           resultado = num1 / num2;
      //           printf("%2.f %c %2.f = %2.f", num1, operador, num2, resultado);
      //         }; break;
      // }

//     printf("\nDeseja fazer outra operação(s/n): ");
//     scanf("%c", &sair);
//   }
// }

// MEDIA

// int main(void) {

//   float nota1, nota2, media;

//   printf("Escreva sua primeira e sua segunda nota: ");
//   scanf("%f %f", &nota1, &nota2);

//   media = (nota1 + nota2) / 2;

//   if(media >= 7){
//     printf("Você foi aprovado!");
//   } else if (media >= 6){
//     printf("Você vai para a final!");
//   } else {
//     printf("Você está reprovado!");
//   }
// }

// PAR CRESCENTE

// int main(void){
//   int limite;
//   int inicial = 0;
  
//   printf("Digite um número: ");
//   scanf("%i", &limite);

//   while(inicial <= limite){
//     printf("\n%i", inicial);
//     inicial += 2;
//   }
// }

// PAR DECRESCENTE

int main(void){
  int inicial;

  printf("Digite um número: ");
  scanf("%i", &inicial);

  while(inicial > 0){
    if(inicial % 2 != 0){
      inicial -= 1;
      printf("\n%i", inicial);
    } else {
      inicial -= 2;
      printf("\n%i", inicial);
    }
  }
}