//
// Created by gabrielbelo on 28/05/25.
//

#include <stdio.h>

void main()
{
    float total_compra;
    float cliente_pagou;

    printf("Digite o valor da compra: ");
    scanf("%f", &total_compra);

    printf("Digite o valor pago pelo cliente: ");
    scanf("%f", &cliente_pagou);

    float troco_float = total_compra - cliente_pagou;

    if (troco_float == 0)
    {
        printf("Troco: 0.0");
    }
    else if (troco_float < 0)
    {
        float troco_entregue = 0;
        troco_float *= -1;
        int troco_centavos = troco_float * 100.01;

        int qtd_cem = 0, qtd_cinquentaR = 0, qtd_vinte = 0, qtd_dezR = 0, qtd_cincoR = 0, qtd_dois = 0,
        qtd_umR = 0, qtd_cinquentaC = 0, qtd_vinte_cinco = 0, qtd_dezC = 0, qtd_cincoC = 0, qtd_umC = 0;

        while (troco_centavos > 0)
        {
            if (troco_centavos - 10000 >= 0)
            {
                troco_centavos -= 10000;
                troco_entregue += 100;
                qtd_cem++;
            }
            else if (troco_centavos - 5000 >= 0)
            {
                troco_centavos -= 5000;
                troco_entregue += 50;
                qtd_cinquentaR++;
            }
            else if (troco_centavos - 2000 >= 0)
            {
                troco_centavos -= 2000;
                troco_entregue += 20;
                qtd_vinte++;
            }
            else if (troco_centavos - 1000 >= 0)
            {
                troco_centavos -= 1000;
                troco_entregue += 10;
                qtd_dezR++;
            }
            else if (troco_centavos - 500 >= 0)
            {
                troco_centavos -= 500;
                troco_entregue += 5;
                qtd_cincoR++;
            }
            else if (troco_centavos - 200 >= 0)
            {
                troco_centavos -= 200;
                troco_entregue += 2;
                qtd_dois++;
            }
            else if (troco_centavos - 100 >= 0)
            {
                troco_centavos -= 100;
                troco_entregue += 1;
                qtd_umR++;
            }
            else if (troco_centavos - 50 >= 0)
            {
                troco_centavos -= 50;
                troco_entregue += 0.5;
                qtd_cinquentaC++;
            }
            else if (troco_centavos - 25 >= 0)
            {
                troco_centavos -= 25;
                troco_entregue += 0.25;
                qtd_vinte_cinco++;
            }
            else if (troco_centavos - 10 >= 0)
            {
                troco_centavos -= 10;
                troco_entregue += 0.1;
                qtd_dezC++;
            }
            else if (troco_centavos - 5 >= 0)
            {
                troco_centavos -= 5;
                troco_entregue += 0.05;
                qtd_cincoC++;
            }
            else if (troco_centavos - 1 >= 0)
            {
                troco_centavos -= 1;
                troco_entregue += 0.01;
                qtd_umC++;
            }
        }
        printf("Troco: R$%.2f", troco_entregue);
        printf(" \nNotas de R$100: %i\n Notas de R$50: %i\n Notas de R$20: %i\n Notas de R$10: %i\n Notas de R$5: %i\n Notas de R$2: %i\n Notas de R$1: %i", qtd_cem, qtd_cinquentaR, qtd_vinte, qtd_dezR, qtd_cincoR, qtd_dois, qtd_umR);
        printf("\n_________________");
        printf(" \nMoedas de R$0.50: %i\n Moedas de R$0.25: %i\n Moedas de R$0.10: %i\n Moedas de R$0.05: %i\n Moedas de R$0.01: %i", qtd_cinquentaC, qtd_vinte_cinco, qtd_dezC, qtd_cincoC, qtd_umC);
    }
}