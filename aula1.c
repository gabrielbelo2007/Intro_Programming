#include <stdio.h>

int main(void) {
  // printf("Eu adoro programar em C!");

  // int numero_inteiro = 10;
  // float numero_fracionado = 10.5;
  // char caractere = 'a';

  // printf("O valor da variável numero_inteiro é: %d\n", numero_inteiro);
  // printf("O valor da variável numero_fracionado é: %f\n", numero_fracionado);
  // printf("O valor da variável caractere é: %c\n", caractere);

  // printf("A posição da memória de numero_inteiro é: %p\n", &numero_inteiro);

  // int idade;
  // printf("Digite a sua idade: ");
  // scanf("%i", &idade);
  // printf("\nA sua idade é: %i", idade);

  int dia;
  int mes;
  int ano;

  printf("Escreva o dia, o mês e o ano que você nasceu: ");
  scanf("%i %i %i", &dia, &mes, &ano);
  printf("\nVocê nasceu no dia %i no mês %i do ano %i!", dia, mes, ano);
  return 0;
}