#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

typedef struct {
    char titulo[100];
    char codigo_filme[21];
    int quatidade_disponivel;
    int n_alugueis;
    int n_devolucoes;
    float preco_aluguel;
    int status;
} Filme;

Filme criarFilme(Filme filmes[], int *posicao){
    Filme novo_filme;
    printf("\n--- Cadastrar Filme --- \n");

    printf("Digite o título do filme: ");
    scanf("%s", novo_filme.titulo);
    getchar();

    do{
        char codigo_digitado[21];
        printf("Digite o código do filme(máx 20 caracteres): ");  

        if(buscar(filmes, codigo_digitado, posicao) != -1){
            printf("Código já cadastrado. Tente novamente.\n");
            continue;
        }

        if(fgets(codigo_digitado, sizeof(codigo_digitado), stdin))
        {
            char* checando_tamanho = strchr(codigo_digitado, '\n');
            if (checando_tamanho)
            {
                *checando_tamanho = '\0';
                strcpy(novo_filme.codigo_filme, codigo_digitado);
                break;
            } 
            else 
            {
                printf("O código digitado é muito longo. Tente novamente.\n");
                getchar();
                continue;
            }
        }
        else 
        {
            printf("Erro ao ler o código do filme. Tente novamente.\n");
            continue;
        }
    }while(1);

    printf("Digite o preço do aluguel: ");
    scanf("%f", &novo_filme.preco_aluguel);
    getchar();

    novo_filme.quatidade_disponivel = 0;
    novo_filme.n_alugueis = 0;
    novo_filme.n_devolucoes = 0;
    novo_filme.status = 1;

    return novo_filme;
}

int inserir(Filme filmes[], Filme novo_filme, int tam, int *posicao){
    if(*posicao < tam){
        filmes[*posicao] = novo_filme;
        (*posicao)++; // Verificar isso aqui no meu código anterior
        printf("Filme cadastrado com sucesso!\n");
        return 1;
    } else {
        printf("Não é possível cadastrar mais filmes. Limite atingido.\n");
        return 0;
    }
}	

int buscar(Filme filmes[], char codigo_filme[], int posicao){
    for(int i = 0; i < posicao; i++){
        if(strcmp(filmes[i].codigo_filme, codigo_filme) == 0){
            return i;
        }
    }
    return -1;
}

int remover(Filme filmes[], char codigo_filme[], int posicao){
    int posicao = buscar(filmes, codigo_filme, posicao);

    if(posicao != -1){
        filmes[posicao].status = 0;
        printf("Filme removido com sucesso!\n");
        return 1;
    }

    printf("Filme não encontrado.\n");
    return 0;
}

int comprar(Filme filmes[], char codigo_filme[], int posicao, int quantidade){
    int posicao = buscar(filmes, codigo_filme, posicao);

    if(posicao != -1){
        filmes[posicao].quatidade_disponivel += quantidade;
        printf("Compra realizada com sucesso!\n");
        return 1;
    }

    printf("Filme não encontrado.\n");
    return 0;
}

int alugar(Filme filmes[], char codigo_filme[], int posicao){
    int posicao = buscar(filmes, codigo_filme, posicao);

    if(posicao != -1){
        if(filmes[posicao].quatidade_disponivel > 0){
            filmes[posicao].quatidade_disponivel--;
            filmes[posicao].n_alugueis++;
            printf("Filme alugado com sucesso!\n");
            return 1;
        } else {
            printf("Filme indisponível para aluguel.\n");
            return 0;
        }
    }

    printf("Filme não encontrado.\n");
    return 0;
}

int devolver(Filme filmes[], char codigo_filme[], int posicao){
    int posicao = buscar(filmes, codigo_filme, posicao);

    if(posicao != -1){
        filmes[posicao].quatidade_disponivel++;
        filmes[posicao].n_devolucoes++;
        printf("Filme devolvido com sucesso!\n");
        return 1;
    }

    printf("Filme não encontrado.\n");
    return 0;
}

int main(){
    setlocale(LC_ALL, "Portuguese");

    int posicao = 0;
    int tam = 2;
    Filme filmes[tam];
    
    char opcao;
    char fechar = 'n';
    printf("--- Bem-vindo ao sistema de locadora de filmes! ---\n");

    do{
        printf("Você pode cadastrar(c), remover(r), comprar(c), alugar(a) e devolver filmes(d).\n");
        printf("Digite a opção desejada: ");
        scanf("%c", &opcao);
        getchar();

        if(tolower(opcao) == 'c')
        {
            int n_filmes;
            do{
                printf("Quantos filmes deseja cadastrar? ");
                scanf("%i", &n_filmes);
                getchar();

                if(n_filmes <= 0){
                    printf("Número de filmes deve ser maior que zero.\n");
                }
            }while(n_filmes <= 0);

            for(int i = 0; i < n_filmes; i++){
                Filme filme_criado = criarFilme(filmes, &posicao);
                int inserido = inserir(filmes, filme_criado, tam, &posicao);

                if(!inserido){
                    break;
                }
            }
        }
        else if(tolower(opcao) == 'r')
        {
            
            char codigo_filme[21];
            char* checando_tamanho;
            do{
                printf("Digite o código do filme a ser removido: ");

                if(fgets(codigo_filme, sizeof(codigo_filme), stdin)){
                    checando_tamanho = strchr(codigo_filme, '\n');
                }
                else
                {
                    printf("Escolha um código válido.\n");
                    continue;
                }
            }while(checando_tamanho == NULL);
            remover(filmes, codigo_filme, posicao);
        }
        else if(tolower(opcao) == 'b')
        {
            char codigo_filme[21];
            printf("Digite o código do filme a ser comprado: ");
            fgets(codigo_filme, sizeof(codigo_filme), stdin);
            codigo_filme[strcspn(codigo_filme, "\n")] = 0; // Remove newline

            int quantidade;
            printf("Quantos filmes deseja comprar? ");
            scanf("%i", &quantidade);
            getchar();

            comprar(filmes, codigo_filme, posicao, quantidade);
        }
        else if(tolower(opcao) == 'a')
        {
            char codigo_filme[21];
            printf("Digite o código do filme a ser alugado: ");
            fgets(codigo_filme, sizeof(codigo_filme), stdin);
            codigo_filme[strcspn(codigo_filme, "\n")] = 0; // Remove newline

            alugar(filmes, codigo_filme, posicao);
        }
        else if(tolower(opcao) == 'd')
        {
            char codigo_filme[21];
            printf("Digite o código do filme a ser devolvido: ");
            fgets(codigo_filme, sizeof(codigo_filme), stdin);
            codigo_filme[strcspn(codigo_filme, "\n")] = 0; // Remove newline

            devolver(filmes, codigo_filme, posicao);
        }
        else{
            printf("Digite uma opção válida.\n");
        }

        printf("Deseja continuar? (s/n): ");
        scanf("%c", &opcao);
        getchar();
    }while(tolower(opcao) != 's');

    return 1;
}
