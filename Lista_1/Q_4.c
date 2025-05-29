#include <stdio.h>

void main()
{
    int numero;

    printf("Tamanho do quadrado: ");
    scanf("%i", &numero);

    if (numero % 2 == 0)  // Numero = par
    {
        int espaco_meio =  numero - 2;
        int espaco_inicio = 0;

        for (int tamanho = numero; tamanho > 0; --tamanho)
        {
            // Metada - 1
            if(tamanho > numero / 2){
                printf("x");
                for (int x = 0; x < espaco_meio; x++)
                {
                    printf(" ");
                }
                printf("x\n");

                if(espaco_meio - 2 >= 0){
                    espaco_meio -= 2;
                }
                
                if(espaco_inicio + 1 <= numero - (numero/2 + 1)){
                    ++espaco_inicio;

                    for (int y = 0; y < espaco_inicio; y++)
                    {
                        printf(" ");
                    }
                }
            }

            // Metade -> Fim
            else{
                
                for (int y = 0; y < espaco_inicio; y++)
                {
                    printf(" ");
                }
                --espaco_inicio;
    
                printf("x");
                for (int x = 0; x < espaco_meio; x++)
                {
                    printf(" ");
                }
                printf("x\n");
                espaco_meio += 2;
            }
        }
    }
    
    else  // Numero = impar
    {
        int espaco_meio = numero - 2;
        int espaco_inicio = 0;

        // Inicio -> Metade
        for (int tamanho = numero; tamanho > 0; tamanho--)
        {
            if (tamanho > numero / 2){ // 3
                printf("x");
                for (int x = 0; x < espaco_meio; x++)
                {
                    printf(" ");
                }
                if(tamanho != (numero / 2 + 1)){
                    printf("x\n");
                }
                else if(tamanho == (numero / 2 + 1))
                {
                    printf("\n");
                }
    
                if(espaco_meio - 2 >= 0){
                    espaco_meio -= 2;
                }
    
                if(espaco_inicio + 1 <= numero - (numero/2 + 1)){
                    ++espaco_inicio;
    
                    for (int y = 0; y < espaco_inicio; y++)
                    {
                        printf(" ");
                    }
                }
            }
            
            // Metade -> Fim
            else
            {
                espaco_inicio--;
                for (int y = 0; y < espaco_inicio; y++)
                {
                    printf(" ");
                }

                printf("x");
                for (int x = 0; x < espaco_meio; x++)
                {
                    printf(" ");
                }
                printf("x\n");
                espaco_meio += 2;
            }
        }
    }
}
