#include <stdio.h>
#include <string.h>
#include <ctype.h>

typedef struct {
    char titulo[100];
    char codigo_filme[21];
    int quantidade_disponivel;
    int n_alugueis;
    int n_devolucoes;
    float preco_aluguel;
    int status;
} Filme;

int buscar(Filme filmes[], char codigo_filme[], int tamanho_usado){
    for(int i = 0; i < tamanho_usado; i++){
        if(strcmp(filmes[i].codigo_filme, codigo_filme) == 0 && filmes[i].status == 1){
            return i;
        }
    }
    return -1;
}

Filme criarFilme(Filme filmes[], int posicao){
    Filme novo_filme;
    printf("\n--- Cadastrar Filme --- \n");

    printf("Digite o título do filme: ");
    scanf("%s", novo_filme.titulo);
    getchar();

    do{
        char codigo_digitado[21];
        printf("Digite o código do filme: ");
        scanf("%s", codigo_digitado);

        if(buscar(filmes, codigo_digitado, posicao) != -1){
            printf("Código já cadastrado. Tente novamente.\n");
        }
        else
        {
            strcpy(novo_filme.codigo_filme, codigo_digitado);
            break;
        }
    }while(1);

    printf("Digite o preço do aluguel: ");
    scanf("%f", &novo_filme.preco_aluguel);
    getchar();

    novo_filme.quantidade_disponivel = 0;
    novo_filme.n_alugueis = 0;
    novo_filme.n_devolucoes = 0;
    novo_filme.status = 1;

    return novo_filme;
}

int inserir(Filme filmes[], Filme novo_filme, int tam, int *posicao){
    if(*posicao < tam){
        filmes[*posicao] = novo_filme;
        (*posicao)++;
        return 1;
    }
    return 0;
}

int remover(Filme filmes[], char codigo_filme[], int tamanho_usado){
    int posicao = buscar(filmes, codigo_filme, tamanho_usado);

    if(posicao != -1){
        filmes[posicao].status = 0;
        return 1;
    }
    return 0;
}

int comprar(Filme filmes[], char codigo_filme[], int tamanho_usado, int quantidade){
    int posicao = buscar(filmes, codigo_filme, tamanho_usado);

    if(posicao != -1){
        filmes[posicao].quantidade_disponivel += quantidade;
        return 1;
    }
    return 0;
}

int alugar(Filme filmes[], char codigo_filme[], int tamanho_usado){
    int posicao = buscar(filmes, codigo_filme, tamanho_usado);

    if(posicao != -1){
        if(filmes[posicao].quantidade_disponivel > 0){
            filmes[posicao].quantidade_disponivel--;
            filmes[posicao].n_alugueis++;
            return 1;
        }
        return 0;
    }
    return 0;
}

int devolver(Filme filmes[], char codigo_filme[], int tamanho_usado){
    int posicao = buscar(filmes, codigo_filme, tamanho_usado);

    if(posicao != -1){
        filmes[posicao].quantidade_disponivel++;
        filmes[posicao].n_devolucoes++;
        return 1;
    }
    return 0;
}

// Lista todos os filmes ativos
int listarEstoque(Filme filmes[], int tamanho_usado, int vai_alugar){

    //Checa se tem filmes ativos
    if (vai_alugar == -1)
    {
        int filme_ativo = 0;
        for(int i = 0; i < tamanho_usado; i++){
            if(filmes[i].status == 1){
                filme_ativo = 1;
            }
        }
        return filme_ativo;
    }

    // Mostra apenas os filmes ativos, para as funções que não sejam alugar
    if (vai_alugar == 0)
    {
        printf("\n\n--- Lista de Filmes ---\n");
        for(int i = 0; i < tamanho_usado; i++){
            if(filmes[i].status == 1){
                printf("Título: %s | Quantidade Disponível: %i | Preço do Aluguel: %.2f | Código: %s\n", filmes[i].titulo, filmes[i].quantidade_disponivel, filmes[i].preco_aluguel, filmes[i].codigo_filme);
            }
        }
        return 1;
    }

    // Mostra para alugar, apenas filmes com quantidade > 0
    int tem_filmes = 0;
    printf("\n\n--- Lista de Filmes ---\n");

    for(int i = 0; i < tamanho_usado; i++)
    {
        if(filmes[i].status == 1 && filmes[i].quantidade_disponivel > 0){
            printf("Título: %s | Quantidade Disponível: %i | Preço do Aluguel: %.2f | Código: %s\n", filmes[i].titulo, filmes[i].quantidade_disponivel, filmes[i].preco_aluguel, filmes[i].codigo_filme);
            tem_filmes = 1;
        }
    }
    return tem_filmes;
}

void listarMaisAlugados(Filme filmes[], int tamanho_usado)
{
    printf("\n---Lista de AlugueSis---\n");

    // Criando um vetor para salvar os alugueis desorganizados
    int alugueis_desordenado[tamanho_usado];
    for (int i = 0; i < tamanho_usado; i++)
    {
        alugueis_desordenado[i] = filmes[i].n_alugueis;
    }

    int indice_ordenacao = -1;
    for (int indice_desordenado = 0; indice_desordenado < tamanho_usado; indice_desordenado++)
    {
        int mudou = 0;
        int alugueis_temp = alugueis_desordenado[indice_desordenado];

        for (int indice_ordenado = 0; indice_ordenado < tamanho_usado; indice_ordenado++)
        {
            if (alugueis_desordenado[indice_ordenado] > alugueis_temp)
            {
                alugueis_temp = alugueis_desordenado[indice_ordenado];
                indice_ordenacao = indice_ordenado;
                mudou = 1;
            }
        }
        indice_ordenacao = (mudou == 0) ? indice_desordenado : indice_ordenacao;
        printf("Título: %s | Aluguéis: %i", filmes[indice_ordenacao].titulo, filmes[indice_ordenacao].n_alugueis);

        // Assim os valores já visto como maiores vão ficar menores que os demais
        alugueis_desordenado[indice_ordenacao] = -1;
    }
}

void listarMaisDevolvidos(Filme filmes[], int tamanho_usado)
{
    printf("\n---Lista de Devoluções---\n");

    // Criando um vetor para salvar os alugueis desorganizados
    int devolucoes_desordenada[tamanho_usado];
    for (int i = 0; i < tamanho_usado; i++)
    {
        devolucoes_desordenada[i] = filmes[i].n_devolucoes;
    }

    int indice_ordenacao = -1;
    for (int indice_desordenado = 0; indice_desordenado < tamanho_usado; indice_desordenado++)
    {
        int mudou = 0;
        int alugueis_temp = devolucoes_desordenada[indice_desordenado];

        for (int indice_ordenado = 0; indice_ordenado < tamanho_usado; indice_ordenado++)
        {
            if (devolucoes_desordenada[indice_ordenado] > alugueis_temp)
            {
                alugueis_temp = devolucoes_desordenada[indice_ordenado];
                indice_ordenacao = indice_ordenado;
                mudou = 1;
            }
        }
        indice_ordenacao = (mudou == 0) ? indice_desordenado : indice_ordenacao;
        printf("Título: %s | Devoluções: %i;n", filmes[indice_ordenacao].titulo, filmes[indice_ordenacao].n_devolucoes);

        // Assim os valores já visto como maiores vão ficar menores que os demais
        devolucoes_desordenada[indice_ordenacao] = -1;
    }
}

void extratoFinanceiro(Filme filmes[], int tamanho_usado)
{
    float arrecadado = 0;

    for (int i = 0; i < tamanho_usado; i++)
    {
        arrecadado += (filmes[i].n_alugueis * filmes[i].preco_aluguel);
    }

    printf("\nO total arrecadado foi: %.2f", arrecadado);
}

int main(){

    int posicao = 0;
    int tam = 3;
    Filme filmes[tam];
    
    char opcao;
    printf("--- Bem-vindo ao sistema de locadora de filmes! ---");

    do{
        printf("\nCadastrar(c)\nPor no estoque(p)\nAlugar(a)\nDevolver(d)\nRemover do Sistema(r)\n");
        printf("Digite a opção desejada: ");
        scanf("%c", &opcao);
        getchar();

        // Cadastrar filmes
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
                Filme filme_criado = criarFilme(filmes, posicao);

                int inserido = inserir(filmes, filme_criado, tam, &posicao);
                if (inserido)
                {
                    printf("Filme cadastrado com sucesso\n");
                }
                else
                {
                    printf("Filme não cadastrado, limite de filmes atingido!");
                    break;
                }
            }
        }

        else if (posicao == 0 || listarEstoque(filmes, posicao, -1) == 0)
        {
            printf("O sistema está sem livros ativos!");
        }

        // Remover filmes do estoque
        else if(tolower(opcao) == 'r')
        {
            printf("\n--REMOVER FILME--\n");

            listarEstoque(filmes, posicao, 0);

            char codigo_filme[21];
            printf("Digite o codigo do filme que deseja remover: ");
            scanf("%s", codigo_filme);
            getchar();

            int removido = remover(filmes, codigo_filme, posicao);
            if (removido)
            {
                printf("Filme removido com sucesso");
            }
            else
            {
                printf("Filme não encontrado, verifique o código digitado!");
            }
        }

        // Adicionar filmes no estoque
        else if(tolower(opcao) == 'p')
        {
            printf("\n--ADICIONAR FILME--\n");

            listarEstoque(filmes, posicao, 0);

            char codigo_filme[21];
            printf("\nDigite o codigo do filme que deseja adicionar: ");
            scanf("%s", codigo_filme);

            int quantidade;
            do
            {
                printf("Quantos filmes deseja comprar? ");
                scanf("%i", &quantidade);
                getchar();

                if (quantidade <= 0)
                {
                    printf("Quantidade precisa ser maior que 0!\n");
                }
            }while (quantidade <= 0);

            int comprado = comprar(filmes, codigo_filme, posicao, quantidade);
            if (comprado)
            {
                printf("Filmes adicionados com sucesso!");
            }
            else
            {
                printf("Filme não encontrado, verifique o código digitado!");
            }
        }

        // Alugar Filme
        else if(tolower(opcao) == 'a')
        {
            printf("\n--ALUGAR FILME--\n");

            int tem_estoque = listarEstoque(filmes, posicao, 1);
            if (tem_estoque)
            {
                char codigo_filme[21];
                printf("Digite o código do filme que deseja alugar: ");
                scanf("%s", codigo_filme);
                getchar();

                int alugado = alugar(filmes, codigo_filme, posicao);
                if (alugado)
                {
                    printf("Filme alugado com sucesso!");
                }
                else
                {
                    printf("Filme indisponível");
                }
            }
            else
            {
                printf("Não tem filmes no estoque!");
            }
        }

        // Devolver Filme
        else if(tolower(opcao) == 'd')
        {
            printf("\n--DEVOLVER FILME--\n");

            listarEstoque(filmes, posicao, 0);

            char codigo_filme[21];
            printf("Digite o codigo do filme que deseja devolver: ");
            scanf("%s", codigo_filme);
            getchar();

            int devolvido = devolver(filmes, codigo_filme, posicao);
            if (devolvido)
            {
                printf("Filme devolvido com sucesso!");
            }
            else
            {
                printf("Filme não encontrado, verifique o código digitado!");
            }
        }

        else{
            printf("Digite uma opção válida.\n");
        }

        printf("\n\nDeseja encerrar? (s/n): ");
        scanf("%c", &opcao);
        getchar();
    }while(tolower(opcao) != 's');

    listarEstoque(filmes, posicao, 1);
    listarMaisAlugados(filmes, posicao);
    listarMaisDevolvidos(filmes, posicao);
    extratoFinanceiro(filmes, posicao);

    return 1;
}
