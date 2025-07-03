#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

typedef struct
{
    char numero[3];
    float saldo;
}Conta;

void main(void) {

    int qtd_contas = 1;
    Conta contas[qtd_contas];
    
    for(int i = 0; i < qtd_contas; i++){
        printf("Registre sua conta:\n\n");
        char numero_digitado[2];
        float saldo_solicitado;

        printf("Digite os 2 dígitos da conta: ");
        scanf("%s", contas[i].numero);
        getchar();

        printf("Digite o saldo da sua conta: ");
        scanf("%f", &contas[i].saldo);
        getchar();

        printf("Conta %s registrada com sucesso!\n\n");
    }
    
    while(1){
        
        int existe = 0;
        char acessar_conta[3];
        printf("\nQual conta você deseja acessar: (Listar as contas, digite 'v')\n");
        scanf("%s", acessar_conta);
        getchar();

        char numero_conta[3];
        float saldo_conta;
        int registro_conta = 0;
        
        for(int i = 0; i < qtd_contas; i++){
            if(strcmp(contas[i].numero, acessar_conta) == 0){
                registro_conta = i;
                saldo_conta = contas[i].saldo;
                strcpy(numero_conta, contas[i].numero);
                break;
            }
        }

        if(registro_conta == 0){
            printf("Essa conta não está registrada!\n");
            continue;
        }

        char operacao;
        printf("\n\nQual operação você deseja: Saldo (s) | Creditar (c) | Debitar (d) | Ver contas (v) : ");
        scanf("%c", &operacao);
        getchar();

        float valor;
        
        switch(operacao)
        {
            case 'v':
                for(int i = 0; i < qtd_contas; i++){
                    printf("%s\n", contas[i].numero);
                    printf("%.2f\n\n", contas[i].saldo);        
                }
                break;

            case 's':
                printf("O saldo da sua conta é: %f", saldo_conta);
                break;

            case 'c':
                printf("Digite o valor a ser creditado: ");
                scanf("%f", &valor);
                getchar();

                contas[registro_conta].saldo += valor;

            case 'd':
                printf("Digite o valor a ser debitado: ");
                scanf("%f", &valor);
                getchar();
        }

        char continuar;
        printf("Deseja fazer outra operação? (s)(n)");
        scanf("%c", &continuar);
        getchar();

        if (continuar == 'n'){
            break;
        }
    }
}
