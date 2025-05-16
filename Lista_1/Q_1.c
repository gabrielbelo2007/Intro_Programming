//
// Created by gabrielbelo on 15/05/25.
//

#include <stdio.h>

void main()
{
    int idade;
    int bebida;
    float qtd;
    float gasto = 0;
    float caixa_total = 0;

    char fechar_caixa = 'n';
    while (fechar_caixa == 'n'){

        printf("Digite sua idade: ");
        scanf("%i", &idade);
        getchar();

        if (idade < 18)
        {
            printf("Você é de menor e nao pode comprar bebidas\n");
        } else
        {
            float gasto_temp = 0;
            char cliente_ativo = 's';
            while (cliente_ativo == 's')
            {
                printf("1. Whisky\n");
                printf("2. Vodka\n");
                printf("3. Cerveja\n");
                printf("4. Cachaça\n");
                printf("Escolha a bebida: ");
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
                    scanf("%i %f", &bebida, &qtd);
                    getchar();
                    break;
                case 2:
                    printf("Código Nome Preço\n");
                    printf("200 Vodka1 60\n");
                    printf("201 Vodka2 40\n");
                    printf("202 Vodka3 30\n");
                    printf("Informe código da bebida e a quantidade: ");
                    scanf("%i %f", &bebida, &qtd);
                    getchar();
                    break;
                case 3:
                    printf("Código Nome Preço\n");
                    printf("300 Cerveja1 1.5\n");
                    printf("301 Cerveja2 2.0\n");
                    printf("302 Cerveja3 3.0\n");
                    printf("Informe código da bebida e a quantidade: ");
                    scanf("%i %f", &bebida, &qtd);
                    getchar();
                    break;
                case 4:
                    printf("Código Nome Preço\n");
                    printf("400 Cachaça1 8.0\n");
                    printf("401 Cachaça2 20.0\n");
                    printf("402 Cachaça 22.0\n");
                    printf("Informe código da bebida e a quantidade: ");
                    scanf("%i %f", &bebida, &qtd);
                    getchar();
                    break;
                default:
                    printf("Opção inválida\n");
                    continue;
                }

                switch (bebida)
                {
                case 100:
                    gasto_temp += qtd * 200;
                    break;
                case 101:
                    gasto_temp += qtd * 150;
                    break;
                case 102:
                    gasto_temp += qtd * 140;
                    break;
                case 200:
                    gasto_temp += qtd * 60;
                    break;
                case 201:
                    gasto_temp += qtd * 40;
                    break;
                case 202:
                    gasto_temp += qtd * 30;
                    break;
                case 300:
                    gasto_temp += qtd * 1.5;
                    break;
                case 301:
                    gasto_temp += qtd * 2;
                    break;
                case 302:
                    gasto_temp += qtd * 3;
                    break;
                case 400:
                    gasto_temp += qtd * 8;
                    break;
                case 401:
                    gasto_temp += qtd * 20;
                    break;
                case 402:
                    gasto_temp += qtd * 22;
                    break;
                default:
                    break;
                }

                if (qtd > 5)
                {
                    gasto_temp *= 0.9;
                }
                else if (qtd > 50)
                {
                    gasto_temp *= 0.7;
                }
                else if (qtd > 100)
                {
                    gasto_temp *= 0.65;
                }

                gasto += gasto_temp;
                gasto_temp = 0;

                printf("Deseja registrar mais bebidas para este cliente? (s/n) ");
                scanf("%c", &cliente_ativo);
                getchar();
            }

            printf("\nValor total da compra: R$ %.2f \n", gasto);
            caixa_total += gasto;
            gasto = 0;
        }

        printf("Deseja fechar o caixa? (s/n) ");
        scanf("%c", &fechar_caixa);
    }
    printf("\nTotal apurado no dia: R$ %.2f", caixa_total);
}
