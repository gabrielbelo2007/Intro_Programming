#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main(void) {
    srand(time(NULL));
    int tam = 10;
    char mapa[tam][tam+1];

    for(int i = 0; i < tam; i++){
        for(int j = 0; j < tam; j++){
            mapa[i][j] = ' ';
        }
    }

    int l_r = rand() % tam;
    int c_r = rand() % tam;
    mapa[l_r][c_r] = 'R';

    int x_s, y_s;
    do
    {
        x_s = rand() % tam;
        y_s = rand() % tam;
    } while (x_s == l_r && y_s == c_r);
    mapa[x_s][y_s] = ']';

    for(int zumbis = 0; zumbis < 10;) {
        int x_z = rand() % tam;
        int y_z = rand() % tam;

        if (mapa[x_z][y_z] == ' ')
        {
            mapa[x_z][y_z] = 'Z';
            zumbis++;
        }
    }

    for (int balas = 0; balas < 10;) {
        int x_b = rand() % tam;
        int y_b = rand() % tam;

        if (mapa[x_b][y_b] == ' ') {
            mapa[x_b][y_b] = '-';
            balas++;
        }
    }

    for (int obstaculos = 0; obstaculos < 20;) {
        int x_o = rand() % tam;
        int y_o = rand() % tam;

        if (mapa[x_o][y_o] == ' ')
        {
            mapa[x_o][y_o] = '#';
            obstaculos++;
        }
    }

    int vivo = 1;
    int balas = 0;
    int ganhou = 0;

    do{
        for(int i = 0; i < tam; i++){
            for(int j= 0; j < tam; j++){
                printf("%c ", mapa[i][j]);
            }
            printf("\n");
        }
        printf("\nBalas: %i restante(s)\n", balas);
        
        char move;
        printf("\n> ");
        scanf("%c", &move);
        getchar();
        
        switch(move){
            case 'w':
                if (l_r-1 >= 0)
                {
                    switch (mapa[l_r-1][c_r])
                    {
                        case ' ':
                            mapa[l_r][c_r] = ' ';
                            l_r--;
                            mapa[l_r][c_r] = 'R';
                            break;

                        case 'Z':
                            if (balas == 0)
                            {
                                vivo = 0;
                            } else
                            {
                                balas--;
                                mapa[l_r][c_r] = ' ';
                                l_r--;
                                mapa[l_r][c_r] = 'R';
                            }
                            break;

                        case '-':
                            balas++;
                            mapa[l_r][c_r] = ' ';
                            l_r--;
                            mapa[l_r][c_r] = 'R';
                            break;

                        case ']':
                            ganhou = 1;
                            vivo = 0;
                            break;

                        default:
                            printf("Caminho bloqueado!\n\n");
                    }
                }
                else
                {
                    printf("Fim do mapa, tente outro caminho!\n\n");
                }
            break;
            
            case 's':
                if(l_r+1 <= tam){
                    switch (mapa[l_r+1][c_r])
                    {
                        case ' ':
                            mapa[l_r][c_r] = ' ';
                            l_r++;
                            mapa[l_r][c_r] = 'R';
                            break;

                        case 'Z':
                            if (balas == 0)
                            {
                                vivo = 0;
                            } else
                            {
                                balas--;
                                mapa[l_r][c_r] = ' ';
                                l_r++;
                                mapa[l_r][c_r] = 'R';
                            }
                            break;

                        case '-':
                            balas++;
                            mapa[l_r][c_r] = ' ';
                            l_r++;
                            mapa[l_r][c_r] = 'R';
                            break;

                        case ']':
                            ganhou = 1;
                            vivo = 0;
                            break;

                        default:
                            printf("Caminho bloqueado!\n\n");
                    }
                }
                else
                {
                    printf("Fim do mapa, tente outro caminho!\n\n");
                }
            break;
            
            case 'a':
                if(c_r-1 >= 0){
                    switch (mapa[l_r][c_r-1])
                    {
                        case ' ':
                            mapa[l_r][c_r] = ' ';
                            c_r--;
                            mapa[l_r][c_r] = 'R';
                            break;

                        case 'Z':
                            if (balas == 0)
                            {
                                vivo = 0;
                            } else
                            {
                                balas--;
                                mapa[l_r][c_r] = ' ';
                                c_r--;
                                mapa[l_r][c_r] = 'R';
                            }
                            break;

                        case '-':
                            balas++;
                            mapa[l_r][c_r] = ' ';
                            c_r--;
                            mapa[l_r][c_r] = 'R';
                            break;

                        case ']':
                            ganhou = 1;
                            vivo = 0;
                            break;

                        default:
                            printf("Caminho bloqueado!\n\n");
                    }
                }
                else
                {
                    printf("Fim do mapa, tente outro caminho!\n\n");
                }
            break;
            
            case 'd':
                if(c_r+1 >= 0){
                    switch (mapa[l_r][c_r+1])
                    {
                    case ' ':
                        mapa[l_r][c_r] = ' ';
                        c_r++;
                        mapa[l_r][c_r] = 'R';
                        break;

                    case 'Z':
                        if (balas == 0)
                        {
                            vivo = 0;
                        } else
                        {
                            balas--;
                            mapa[l_r][c_r] = ' ';
                            c_r++;
                            mapa[l_r][c_r] = 'R';
                        }
                        break;

                    case '-':
                        balas++;
                        mapa[l_r][c_r] = ' ';
                        c_r++;
                        mapa[l_r][c_r] = 'R';
                        break;

                    case ']':
                        ganhou = 1;
                        vivo = 0;
                        break;

                    default:
                        printf("Caminho bloqueado!\n\n");
                    }
                }
                else
                {
                    printf("Fim do mapa, tente outro caminho!\n\n");
                }
            break;
        }
    }while(vivo);

    if (ganhou)
    {
        printf("\nVocê escapou!");
    }
    else
    {
        printf("\nVocê morreu!");
    }
}
