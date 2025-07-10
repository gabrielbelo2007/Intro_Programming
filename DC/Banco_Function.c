#include <stdio.h>
#include <string.h>

typedef struct
{
    char numero[3];
    float saldo;
}Conta;

void preencher(Conta contas[], int tam)
{
    for (int i = 0; i < tam; i++)
    {
        printf("Digite o número da sua conta: ");
        scanf("%s", contas[i].numero);
        getchar();

        contas[i].saldo = 0;
    }
}

void imprimir(Conta contas[], int tam)
{
    for(int i = 0; i < tam; i++)
    {
        printf("A conta %s possui R$ %f.\n", contas[i].numero, contas[i].saldo);
    }
    printf("\n");
}

int buscarConta(char numero[], Conta contas[], int tam)
{
    for (int i = 0; i < tam; i++)
    {
        if (strcmp(numero, contas[i].numero) == 0)
        {
            return i;
        }
    }
    return -1;
}

int creditar(char numero[], float valor, Conta contas[], int tam)
{
    int resultadoBusca = buscarConta(numero, contas, 3);

    if (resultadoBusca != -1)
    {
        contas[resultadoBusca].saldo += valor;
        printf("O valor R$ %.2f foi creditado na conta %s.\n", valor, numero);
        printf("Saldo atual: R$ %.2f\n\n", contas[resultadoBusca].saldo);
    }
    return resultadoBusca;
}

int debitar(char numero[], float valor, Conta contas[], int tam)
{
    int resultadoBusca = buscarConta(numero, contas, 3);

    if (resultadoBusca != -1)
    {
        if (contas[resultadoBusca].saldo - valor < 0)
        {
            printf("\nA conta %s não tem saldo suficiente para debitar o valor R$ %.2f\n", contas[resultadoBusca].numero, valor);
            printf("Saldo disponível R$ %.2f\n\n", contas[resultadoBusca].saldo);
            return -2;
        }
        contas[resultadoBusca].saldo -= valor;
    }
    return resultadoBusca;
}

void transferir(char numContaDebitar[], char numContaCreditar[], float valor, Conta contas[], int tam)
{
    int conta_1 = buscarConta(numContaDebitar, contas, tam);
    int conta_2 = buscarConta(numContaCreditar, contas, tam);

    if (conta_1 != -1 )
    {
        if (conta_2 != -1)
        {
            int novoSaldo = debitar(numContaDebitar, valor, contas, tam);

            if (novoSaldo == conta_1)
            {
                printf("O valor R$ %.2f foi debitado da conta %s para a conta %s.\n", valor, numContaDebitar, numContaCreditar);
                creditar(numContaCreditar, valor, contas, tam);
            }
        }
        else
        {
            printf("A conta %s não existe, escolha uma conta válida para creditar!", numContaCreditar);
        }
    }
    else
    {
        printf("A conta %s não existe, escolha uma conta válida para debitar!", numContaDebitar);
    }
}

void main()
{
    Conta contas[3];

    preencher(contas, 3);

    creditar("123", 80, contas,3 );
    debitar("234", 100, contas, 3);

    imprimir(contas, 3);

    transferir("123", "234", 80, contas, 3);
}