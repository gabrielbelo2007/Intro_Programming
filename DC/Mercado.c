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

void imprimir_produtos(Produto estante[], int posicao_estante, int mudar_status){
  for (int produto = 0; produto < posicao_estante; produto++){
    if(estante[produto].status != 0 && mudar_status == 0){
      printf("\nProduto: %s | Preço: %.2f | Código: %i\n", estante[produto].nome, estante[produto].preco, estante[produto].codigo_produto);
    }
    else if (mudar_status == 1)
    {
      printf("\nProduto: %s | Preço: %.2f | Código: %i\n | Status: %i", estante[produto].nome, estante[produto].preco, estante[produto].codigo_produto, estante[produto].status);
    }
  }
}

int buscar_produto(Produto estante[], int codigo_digitado, int tam, int mudar_status){
    for(int i = 0; i < tam; i++){
      if(estante[i].codigo_produto == codigo_digitado && estante[i].status != 0 && mudar_status == 0){
        return i;
      }
      if (estante[i].codigo_produto == codigo_digitado && mudar_status == 1)
      {
        return i;
      }
    }
  return -1;
}

Produto criar_produto(Produto estante[], int tam){

  printf("\n-----Dados do Produto-----\n");
  Produto produto;
  
  printf("Qual o nome do produto? ");
  scanf("%s", produto.nome);
  getchar();

  printf("Qual o preço desse produto? ");
  scanf("%f", &produto.preco);
  getchar();

  int codigo;
  int id_unico;
  do
  {
    printf("Qual o código desse produto? ");
    scanf("%i", &codigo);
    getchar();

    id_unico = buscar_produto(estante, codigo, tam, 1);
    if (id_unico != -1)
    {
      printf("Esse código já está em uso!\n");
    }
  }while (id_unico != -1);

  produto.n_compras = 0;
  produto.codigo_produto = codigo;
  produto.quantidade_disponivel = 0;
  produto.n_vendas = 0;
  produto.status = 1;

  return produto;
}

void inserir_produto_estante(Produto produto, Produto estante[], int *posicao_estante){
    int posicao = *posicao_estante;
    estante[posicao] = produto;

    *posicao_estante += 1;
}

int comprar(Produto estante[], int codigo_produto, int qtd_comprada, int tam_estante, float *valor_comprado){
  int posicao_produto = buscar_produto(estante, codigo_produto, tam_estante, 0);

  estante[posicao_produto].quantidade_disponivel += qtd_comprada;

  *valor_comprado += (estante[posicao_produto].preco * qtd_comprada);
  return 1;
}

int vender(Produto estante[], int codigo_produto, int qtd_vendida, int tam_estante, float *valor_vendido){
  int posicao_produto = buscar_produto(estante, codigo_produto, tam_estante,0);

  estante[posicao_produto].quantidade_disponivel -= qtd_vendida;

  *valor_vendido += (estante[posicao_produto].preco * qtd_vendida);
  return 1;
}

int mudar_status(Produto estante[], int codigo_produto, int tam_estante)
{
  int posicao_produto = buscar_produto(estante, codigo_produto, tam_estante, 1);
  estante[posicao_produto].status = (estante[posicao_produto].status == 0) ? 1 : 0;

  return 1;
}

void main(){

  float valor_gasto = 0;
  float valor_arrecadado = 0;

  char inserir;
  int posicao_estante = 0;
  int tam_estante = 2;
  Produto estante[tam_estante];

  char fechar = 'n';
  printf("Bem vindo ao Gabs's Market!\n\n");

  do
  {
    printf("\nInserir produtos (i) | Mudar status (m) | Comprar produtos (c) | Vender produtos (v): ");

    scanf("%c", &inserir);
    getchar();

    // Inserir produto na estante
    if(inserir == 'i' && posicao_estante <= (tam_estante - 1)){

      int qtd_produtos = 0;
      do
      {
        printf("\nQuantos produtos você deseja inserir: ");
        scanf("%i", &qtd_produtos);
        getchar();

        if(qtd_produtos <= 0){
          printf("Digite uma quantidade válida!");
          continue;
        }

        if ((tam_estante - posicao_estante) < qtd_produtos)
        {
          printf("A estante não tem esse espaço, espaço disponível: %i", tam_estante - posicao_estante);
          continue;
        }

        break;
      } while (1);

      for(int inseridos = 0; inseridos < qtd_produtos; inseridos++)
      {
        inserir_produto_estante(criar_produto(estante, tam_estante), estante, &posicao_estante);
      }
    }

    else if (inserir == 'i' && posicao_estante == tam_estante)
    {
      printf("A estante já está cheia, não é possível mais adicionar novos produtos!");
    }

    // Mudar Status do produto
    else if (inserir == 'm')
    {
      int codigo_alterar;
      do
      {
        imprimir_produtos(estante, posicao_estante, 1);

        printf("\nDigite o código do produto que você quer alterar: ");
        scanf("%i", &codigo_alterar);
        getchar();

        if (buscar_produto(estante, codigo_alterar, tam_estante, 1) == -1)
        {
          printf("Digite um código válido!");
          continue;
        }
        break;
      }while (1);

      mudar_status(estante, codigo_alterar, tam_estante);
    }

    // Comprar produto
    else if (inserir == 'c')
    {
      int qtd_comprar;
      int codigo_comprar;
      do
      {
        imprimir_produtos(estante, posicao_estante, 0);

        printf("\nDigite o código do produto que você quer comprar: ");
        scanf("%i", &codigo_comprar);
        getchar();

        if (buscar_produto(estante, codigo_comprar, tam_estante, 0) == -1)
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

      comprar(estante, codigo_comprar, qtd_comprar, tam_estante, &valor_gasto);
    }

    // Vender produto
    else if (inserir == 'v')
    {
      int qtd_vender;
      int codigo_comprar;
      do
      {
        imprimir_produtos(estante, posicao_estante, 0);

        printf("\nDigite o código do produto que você quer comprar: ");
        scanf("%i", &codigo_comprar);
        getchar();

        if (buscar_produto(estante, codigo_comprar, tam_estante, 0) == -1)
        {
          printf("Digite um código válido!");
          continue;
        }
        break;
      }while (1);

      do
      {
        int posicao_produto_estante = buscar_produto(estante, codigo_comprar, tam_estante, 0);
        int qtd_disponivel_produto = estante[posicao_produto_estante].quantidade_disponivel;

        if (qtd_disponivel_produto == 0)
        {
          printf("Não temos estoque desse produto!");
          break;
        }

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

      vender(estante, codigo_comprar, qtd_vender, tam_estante, &valor_arrecadado);
    }

    else
    {
      printf("%c", inserir);
      printf("Escolha uma opção existente!");
    }

    printf("\n\nDeseja fechar o mercado(s/n): ");
    scanf("%c", &fechar);
    getchar();
  }while (fechar == 'n');

  printf("Lucro final: %.2f", valor_arrecadado);
}
