//
// Created by gabrielbelo on 15/05/25.
//

#include <stdio.h>

void main()
{
    int idade, bebida;
    float qtd_bebidas;
    float gasto_cliente = 0, caixa_total = 0;

    char fechar_caixa = 'n';
    while (fechar_caixa == 'n'){

        printf("Digite sua idade: ");
        scanf("%i", &idade);
        getchar();

        if (idade < 18)
        {
            printf("Você é de menor e não pode comprar bebidas\n");
        }

        else
        {
            char cliente_ativo = 's';
            while (cliente_ativo == 's')
            {
                float gasto_temp = 0;
                printf("1. Whisky\n2. Vodka\n3. Cerveja\n4. Cachaça\nEscolha a bebida: ");
                scanf("%i", &bebida);
                getchar();

                switch (bebida)
                {
                case 1:
                    printf("Código Nome Preço\n");
                    printf("100 Whisky1 200\n");
                    printf("101 Whisky2 150\n");
                    printf("102 Whisky3 140\n");
                    printf("Informe código da bebida e a quantidade: ");
                    scanf("%i %f", &bebida, &qtd_bebidas);
                    getchar();
                    break;
                case 2:
                    printf("Código Nome Preço\n");
                    printf("200 Vodka1 60\n");
                    printf("201 Vodka2 40\n");
                    printf("202 Vodka3 30\n");
                    printf("Informe código da bebida e a quantidade: ");
                    scanf("%i %f", &bebida, &qtd_bebidas);
                    getchar();
                    break;
                case 3:
                    printf("Código Nome Preço\n");
                    printf("300 Cerveja1 1.5\n");
                    printf("301 Cerveja2 2.0\n");
                    printf("302 Cerveja3 3.0\n");
                    printf("Informe código da bebida e a quantidade: ");
                    scanf("%i %f", &bebida, &qtd_bebidas);
                    getchar();
                    break;
                case 4:
                    printf("Código Nome Preço\n");
                    printf("400 Cachaça1 8.0\n");
                    printf("401 Cachaça2 20.0\n");
                    printf("402 Cachaça3 22.0\n");
                    printf("Informe código da bebida e a quantidade: ");
                    scanf("%i %f", &bebida, &qtd_bebidas);
                    getchar();
                    break;
                default:
                    printf("Opção inválida\n");
                    continue;
                }

                switch (bebida)
                {
                case 100:
                    gasto_temp += qtd_bebidas * 200;
                    break;
                case 101:
                    gasto_temp += qtd_bebidas * 150;
                    break;
                case 102:
                    gasto_temp += qtd_bebidas * 140;
                    break;
                case 200:
                    gasto_temp += qtd_bebidas * 60;
                    break;
                case 201:
                    gasto_temp += qtd_bebidas * 40;
                    break;
                case 202:
                    gasto_temp += qtd_bebidas * 30;
                    break;
                case 300:
                    gasto_temp += qtd_bebidas * 1.5;
                    break;
                case 301:
                    gasto_temp += qtd_bebidas * 2;
                    break;
                case 302:
                    gasto_temp += qtd_bebidas * 3;
                    break;
                case 400:
                    gasto_temp += qtd_bebidas * 8;
                    break;
                case 401:
                    gasto_temp += qtd_bebidas * 20;
                    break;
                case 402:
                    gasto_temp += qtd_bebidas * 22;
                    break;
                default:
                    printf("Opção inválida\n");
                    continue;
                }

                if (qtd_bebidas > 5)
                {
                    gasto_temp *= 0.9;
                }
                else if (qtd_bebidas > 50)
                {
                    gasto_temp *= 0.7;
                }
                else if (qtd_bebidas > 100)
                {
                    gasto_temp *= 0.65;
                }

                gasto_cliente += gasto_temp;

                printf("Deseja registrar mais bebidas para este cliente? (s/n) ");
                scanf("%c", &cliente_ativo);
                getchar();
            }

            printf("\nValor total da compra: R$ %.2f \n", gasto_cliente);
            caixa_total += gasto_cliente;
            gasto_cliente = 0;
        }

        printf("Deseja fechar o caixa? (s/n) ");
        scanf("%c", &fechar_caixa);
    }
    printf("\nTotal apurado no dia: R$ %.2f", caixa_total);
}
