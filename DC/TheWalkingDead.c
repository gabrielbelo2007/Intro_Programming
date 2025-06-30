#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main(void) {
    srand(time(NULL));
    int tam = 20;
    char mapa[tam][tam+1];

    for(int i = 0; i < tam; i++){
        for(int j= 0; j < tam; j++){
            mapa[i][j] = ' ';
        }
    }

    int x_r = rand() % tam;
    int y_r = rand() % tam;
    mapa[x_r][y_r] = 'R';

    int x_s = rand() % tam;
    int y_s = rand() % tam;
    while (x_s == x_r && y_s == y_r){
        x_s = rand() % tam;
        y_s = rand() % tam;
    }
    mapa[x_s][y_s] = 'O';

    for(int zumbis = 0; zumbis < 10;  zumbis++) {
        int x_z = rand() % tam;
        int y_z = rand() % tam;

        if (mapa[x_z][y_z] == ' ') {
            mapa[x_z][y_z] = 'Z';
        } else {
            zumbis--;
        }
    }

    for (int balas = 0; balas < 10; balas++) {
        int x_b = rand() % tam;
        int y_b = rand() % tam;

        if (mapa[x_b][y_b] == ' ') {
            mapa[x_b][y_b] = '-';
        } else {
            balas--;
        }
    }

    for (int obstaculos = 0; obstaculos < 20; obstaculos++) {
        int x_o = rand() % tam;
        int y_o = rand() % tam;

        if (mapa[x_o][y_o] == ' ') {
            mapa[x_o][y_o] = '#';
        } else {
            obstaculos--;
        }
    }

    int vivo = 1;

    do{
        for(int i = 0; i < tam; i++){
            for(int j= 0; j < tam; j++){
                printf("%c ", mapa[i][j]);
            }
            printf("\n");
        }
        
        char move;
        printf("\n>");
        scanf("%c", &move);
        getchar();
        
        switch(move){
            case 'w':
                if(x_r-1 >= 0 && mapa[x_r-1][y_r] != '#'){
                    mapa[x_r][y_r] = ' ';
                    x_r--;
                    mapa[x_r][y_r] = 'R';
                }
                break;
            
            case 's':
                if(x_r+1 <= tam && mapa[x_r+1][y_r] != '#'){
                    mapa[x_r][y_r] = ' ';
                    x_r++;
                    mapa[x_r][y_r] = 'R';
                }
                break;
            
            case 'a':
                if(y_r-1 >= 0 && mapa[x_r][y_r-1] != '#'){
                    mapa[x_r][y_r] = ' ';
                    y_r--;
                    mapa[x_r][y_r] = 'R';
                }
                break;
            
            case 'd':
                if(y_r+1 >= 0 && mapa[x_r][y_r+1] != '#'){
                    mapa[x_r][y_r] = ' ';
                    y_r++;
                    mapa[x_r][y_r] = 'R';
                }
                break;
        }
    }while(vivo);
}
