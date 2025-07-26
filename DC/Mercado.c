#include <stdio.h>

typedef struct {
    char nome[100];
    int codigo_produto;
    int quantidade_disponivel;
    int n_vendas;
    int n_compras;
    float preco;
    int status;   //  0 → produto fora do sistema | 1 → produto dentro do sistema
} Produto;

void imprimir_produtos(Produto estante[], int tam){
  for (int produto = 0; produto < tam; produto++){
    if(estante[produto].status != 0){
      printf("\nProduto: %s | Preço: %f | Código: %i\n", estante[produto].nome, estante[produto].preco, estante[produto].codigo_produto);
    }
  }
}

int buscar_produto(Produto estante[], int codigo_digitado, int tam){
    for(int i = 0; i < tam; i++){
      if(estante[i].codigo_produto == codigo_digitado){
        return i;
      } 
    }
  return -1;
}

Produto criar_produto(Produto estante[], int tam){
  Produto produto;
  
  printf("Qual o nome do produto? ");
  scanf("%s", produto.nome);
  getchar();

  printf("\nQuantos você quer inserir desse produto: ");
  scanf("%i", &produto.n_compras);
  getchar();

  printf("Qual o preço desse produto? ");
  scanf("%f", &produto.preco);

  int codigo;
  int id_unico;
  do
  {
    printf("Qual o código desse produto? ");
    scanf("%i", &codigo);
    getchar();

    id_unico = buscar_produto(estante, codigo, tam);
    if (id_unico != -1)
    {
      printf("Esse código já está em uso!");
    }
  }while (id_unico != -1);

  produto.codigo_produto = codigo;
  produto.quantidade_disponivel = 0;
  produto.n_vendas = 0;
  produto.status = 0;

  return produto;
}

void inserir_produto_estante(Produto produto, Produto estante[], int qtd_produtos, int *posicao_estante){
  for (int inseridos = 0; inseridos <= qtd_produtos; inseridos++)
  {
    int posicao = *posicao_estante;
    estante[posicao] = produto;

    *posicao_estante += 1;
  }
}

int comprar(Produto estante[], int codigo_produto, int qtd_comprada, int tam_estante){
  int posicao_produto = buscar_produto(estante, codigo_produto, tam_estante);

  estante[posicao_produto].quantidade_disponivel += qtd_comprada;
  return 1;
}

int vender(Produto estante[], int codigo_produto, int qtd_vendida, int tam_estante){
  int posicao_produto = buscar_produto(estante, codigo_produto, tam_estante);

  estante[posicao_produto].quantidade_disponivel -= qtd_vendida;
  return 1;
}

void main(){

  char inserir;
  int posicao_estante = 0;
  int tam_estante = 2;
  Produto estante[tam_estante];

  char fechar = 'n';
  printf("Bem vindo ao Gabs's Market!\n\n");

  do
  {
    printf("Inserir produtos (i) | Remover produto (r) | Comprar produtos (c) | Vender produtos (v): ");

    scanf("%c", &inserir);
    getchar();

    // Inserir produto na estante
    if(inserir == 'i' && posicao_estante < (tam_estante - 1)){

      int qtd_produtos;
      do
      {
        printf("\nQuantos produtos você deseja inserir: ");
        scanf("%i", &qtd_produtos);
        getchar();

        if(qtd_produtos <= 0){
          printf("Digite uma quantidade válida!");
          continue;
        }

        if ((tam_estante - posicao_estante) <= qtd_produtos)
        {
          printf("A estante não tem esse espaço, espaço disponível: %i", tam_estante - posicao_estante);
          continue;
        }

        break;
      } while (1);

      for(int inseridos = 0; inseridos < qtd_produtos; inseridos++)
      {
        inserir_produto_estante(criar_produto(estante, tam_estante), estante, qtd_produtos, &posicao_estante);
      }
    }

    else if (inserir == 'i' && posicao_estante == (tam_estante - 1))
    {
      printf("A estante já está cheia, não é possível mais adicionar novos produtos!");
    }

    // Remover produto da estante
    // else if (inserir == 'r')
    // {
    //
    // }

    // Comprar produto
    else if (inserir == 'c')
    {
      int qtd_comprar;
      int codigo_comprar;
      do
      {
        imprimir_produtos(estante, tam_estante);

        printf("\nDigite o código do produto que você quer comprar: ");
        scanf("%i", &codigo_comprar);
        getchar();

        if (buscar_produto(estante, codigo_comprar, tam_estante) == -1)
        {
          printf("Digite um código válido!");
          continue;
        }
        break;
      }while (1);

      do
      {

        printf("\nQuantos produtos você deseja comprar: ");
        scanf("%i", &qtd_comprar);
        getchar();

        if(qtd_comprar <= 0)
        {
          printf("Digite uma quantidade válida!");
          continue;
        }

        break;
      } while (1);

      comprar(estante, codigo_comprar, qtd_comprar, tam_estante);
    }

    // Vender produto
    else if (inserir == 'v')
    {
      int qtd_vender;
      int codigo_comprar;
      do
      {
        imprimir_produtos(estante, tam_estante);

        printf("\nDigite o código do produto que você quer comprar: ");
        scanf("%i", &codigo_comprar);
        getchar();

        if (buscar_produto(estante, codigo_comprar, tam_estante) == -1)
        {
          printf("Digite um código válido!");
          continue;
        }
        break;
      }while (1);

      do
      {
        int posicao_produto_estante = buscar_produto(estante, codigo_comprar, tam_estante);
        int qtd_disponivel_produto = estante[posicao_produto_estante].quantidade_disponivel;

        printf("\nQuantos produtos você deseja vender: ");
        scanf("%i", &qtd_vender);
        getchar();

        if(qtd_vender <= 0)
        {
          printf("Digite uma quantidade válida!");
          continue;
        }

        if (qtd_vender > qtd_disponivel_produto)
        {
          printf("O estoque só tem essa quantidade disponível: %i", qtd_disponivel_produto);
          continue;
        }

        break;
      } while (1);

      vender(estante, codigo_comprar, qtd_vender, tam_estante);
    }

    else
    {
      printf("Escolha uma opção existente!");
    }

    printf("\n\nDeseja fechar o mercado(s/n): ");
    scanf("%c", &fechar);
    getchar();
  }while (fechar == 'n');
}
