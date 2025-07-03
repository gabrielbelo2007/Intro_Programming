#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main(void) {
    srand(time(NULL));
    int tam = 8;
    char mapa[tam][tam+1];

    for(int i = 0; i < tam; i++){
        for(int j= 0; j < tam; j++){
            mapa[i][j] = '.';
        }
    }

    int l_c = rand() % tam;
    int c_c = rand() % tam;
    mapa[l_c][c_c] = 'C';

    for(int qtd_pecas = 0; qtd_pecas < 8;){
        int l_p = rand() % 8;
        int c_p = rand() % 8;

        if (mapa[l_p][c_p] == '.'){
            mapa[l_p][c_p] = 'I';
            qtd_pecas++;
        }
    }

    for(int i = 0; i < tam; i++){
        for(int j= 0; j < tam; j++){
            printf("%c ", mapa[i][j]);
        }
        printf("\n");
    }
    printf("\n");

    // MOVIMENTACAO

    int comeu = 0;

    //Pode se mover para cima
    if(l_c - 2 >= 0){
        // Cima - Direita
        if(c_c + 1 <= tam){
            if(mapa[l_c - 2][c_c + 1] == 'I'){
                comeu++;
                printf("%i, %i\n", l_c-1, c_c+2);
            }
        }
        // Cima - Esquerda
        if(c_c - 1 >= 0){
            if(mapa[l_c - 2][c_c - 1] == 'I') 
            {
                comeu++;
                printf("%i, %i\n", l_c-1, c_c);
            }
        }
    }

    //Pode se mover para baixo
    if (l_c + 2 <= tam)
    {
        // Baixo - Direita
        if(c_c + 1 <= tam){
            if(mapa[l_c + 2][c_c + 1] == 'I'){
                comeu++;
                printf("%i, %i\n", l_c+3, c_c+2);
            }
        }
        // Baixo - Esquerda
        if(c_c - 1 >= 0){
            if(mapa[l_c + 2][c_c - 1] == 'I')
            {
                comeu++;
                printf("%i, %i\n", l_c+3, c_c);
            }
        }
    }

    //Pode se mover para esquerda
    if (c_c - 2 >= 0)
    {
        // Esquerda - Cima
        if(l_c - 1 >= 0){
            if(mapa[l_c - 1][c_c - 2] == 'I'){
                comeu++;
                printf("%i, %i\n", l_c, c_c-1);
            }
        }
        // Esquerda - Baixo
        if(l_c + 1 <= tam){
            if(mapa[l_c + 1][c_c - 2] == 'I')
            {
                comeu++;
                printf("%i, %i\n", l_c+2, c_c-1);
            }
        }
    }

    //Pode se mover para direita
    if (c_c + 2 <= tam)
    {
        // Direita - Cima
        if(l_c - 1 >= 0){
            if(mapa[l_c - 1][c_c + 2] == 'I'){
                comeu++;
                printf("%i, %i\n", l_c, c_c+3);
            }
        }
        // Direita - Baixo
        if(l_c + 1 <= tam){
            if(mapa[l_c + 1][c_c + 2] == 'I')
            {
                comeu++;
                printf("%i, %i\n", l_c+2, c_c+3);
            }
        }
    }

    printf("\nPeças abatidas: %i", comeu);
}
