#include <stdio.h>

typedef struct {
    char nome[100];
    int codigo_produto;
    int quantidade_disponivel;
    int n_vendas;
    int n_compras;
    float preco;
    int status;   //  0 -> produto fora do sistema  | 1 -> produto dentro do sistema
} Produto;

void imprimir_produtos(Produto produtos[], int tam){
  for (int i = 0; i < tam; i++){
    if(produtos[i].status != 0){
      printf("\nProduto: %s | Preço: %f | Código: %i\n", produtos[i].nome, produtos[i].preco, produtos[i].codigo_produto);
    }
  }
}

int buscar_produto(Produto produto[], int codigo_digitado, int tam){
    for(int i = 0; i < tam; i++){
      if(produto[i].codigo_produto == codigo_digitado){
        return 1;
      } 
    }
  return 0;
}

Produto criar_produto(){
  Produto produto;
  
  printf("Qual o nome do produto? ");
  scanf("%s", produto.nome);
  getchar();

  printf("\nQuantos você quer inserir desse produto: ");
  scanf("%i", &produto.n_compras);
  getchar();

  printf("Qual o preço desse produto? ");
  scanf("%f", &produto.preco);

  produto.quantidade_disponivel = 0;
  produto.n_vendas = 0;
  produto.status = 0;

  return produto;
}

int inserir_produto_estante(Produto produto, Produto produtos[], int tam, int *posicao_estante){
  int posicao = *posicao_estante;
  produtos[posicao] = produto;

  *posicao_estante += 1;
  return 1;
}

// int comprar(){
  
// }

// int vender(){
  
// }

void main(){

  char inserir;
  int posicao = 0;
  int tam = 2;
  Produto produtos[tam];
  
  printf("Deseja inserir produtos no sistema (s)/(n): ");
  scanf("%c", &inserir);
  getchar();
      
  if(inserir == 's'){
    int qtd_produtos;
    printf("\nQuantos produtos você deseja inserir: ");
    scanf("%i", &qtd_produtos);
    getchar();
    
    if(qtd_produtos <= 0){
      
    }

    else {
      for(int inseridos = 0; inseridos < qtd_produtos; inseridos++)
      {
          inserir_produto_estante(criar_produto(), produtos, qtd_produtos, &posicao); 
      }
    }
    
  }
    
  else{
    
  }

}
