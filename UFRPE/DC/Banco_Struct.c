#include <stdio.h>
#include <string.h>

typedef struct
{
    char numero[3];
    float saldo;
}Conta;

void main(void) {

    int qtd_contas = 3;
    Conta contas[qtd_contas];

    printf("***Banco do Brasil***\n\n");
    for(int i = 0; i < qtd_contas; i++){
        printf("***Registre sua conta***\n");
        char numero_digitado[2];
        float saldo_solicitado;

        printf("Digite os 2 dígitos da conta: ");
        scanf("%s", contas[i].numero);
        getchar();

        printf("Digite o saldo da sua conta: ");
        scanf("%f", &contas[i].saldo);
        getchar();

        printf("Conta %s registrada com sucesso!\n\n",  contas[i].numero);
    }

    while(1){

        int existe = 0;
        char acessar_conta[3];
        printf("\nQual conta você deseja acessar: ");
        scanf("%s", acessar_conta);
        getchar();

        char numero_conta[3];
        float saldo_conta = 0;
        int registro_conta = -1;
        
        for(int i = 0; i < qtd_contas; i++){
            if(strcmp(contas[i].numero, acessar_conta) == 0){
                registro_conta = i;
                saldo_conta = contas[i].saldo;
                strcpy(numero_conta, contas[i].numero);
                break;
            }
        }

        if(registro_conta == -1){
            printf("Essa conta não está registrada!\nContas registradas:\n");
            for(int i = 0; i < qtd_contas; i++){
                printf("%s\n", contas[i].numero);
            }
            continue;
        }

        char operacao;
        printf("\nQual operação você deseja: Saldo (s) | Creditar (c) | Debitar (d): ");
        scanf("%c", &operacao);
        getchar();

        float valor;
        
        switch(operacao)
        {
            case 's':
                printf("O saldo da sua conta é: %.2f\n\n", saldo_conta);
                break;

            case 'c':
                printf("Digite o valor a ser creditado: ");
                scanf("%f", &valor);
                getchar();

                contas[registro_conta].saldo += valor;
                printf("Seu saldo atualizado: %.2f\n\n", contas[registro_conta].saldo);
                break;

            case 'd':
                printf("Digite o valor a ser debitado: ");
                scanf("%f", &valor);
                getchar();

                contas[registro_conta].saldo -= valor;
                printf("Seu saldo atualizado:  %.2f\n\n", contas[registro_conta].saldo);
                break;
        }

        char continuar;
        printf("Deseja fazer outra operação (s)(n)? ");
        scanf("%c", &continuar);
        getchar();

        if (continuar == 'n'){
            printf("\n***Banco do Brasil***");
            break;
        }
    }
}
