#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// void adicionar_elementos(){
    
// }

void inicializar_tabela(int tam, char tabuleiro[tam][tam + 1]){
    for (int l = 0; l < tam; l++){
        for(int c = 0; c < tam; c++){
            tabuleiro[l][c] = '_';
        }
    }
}

void imprimir_mapa(int tam, char tabuleiro[tam][tam + 1]){
    for (int l = 0; l < tam; l++){
        for(int c = 0; c < tam; c++){
            printf("%c", tabuleiro[l][c]);
        }
        printf("\n");
    }
}

void main(){
    int tam = 5;
    char tabuleiro[tam][tam + 1];
    char gabarito[tam][tam + 1];
    
    inicializar_tabela(tam, tabuleiro);
    inicializar_tabela(tam, gabarito);
    imprimir_mapa(tam, tabuleiro);
}
