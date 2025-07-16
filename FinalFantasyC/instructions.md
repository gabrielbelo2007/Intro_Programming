## ======= Final Fantasy =======

### 1) Inicialização dos times

- O usuário atribui o nome para cada lutador da sua equipe.
- Valor randômico para ataque e defesa (valor mínimo é 1).
- A vida de todos os lutadores começa de 100.

### 2) Impressão dos atributos dos lutadores de cada time.

### 3) Sorteio de qual time começa atacando (depois se sucede em turnos de ataque e defesa).

### 4) Ataque

- O time que inicia atacando, escolhe quem do time inimigo o seu lutador irá atacar (as únicas informações que o atacante sabe sobre o oponente é o nome e a vida).

- Cada lutador do time ativo realiza um ataque individualmente, seguindo a ordem de sua equipe.

- O atacante pode errar o ataque a depender da sua precisão, que depende do valor do seu ataque e vida, comparativamente a um número aleatório.

```
precisao = 1 - (lutador_ataque * lutador_vida)/1000;
```

> Informações de defesa e ataque dos oponentes não são mostradas para gerar um "fator surpresa", e exigir atenção durante o jogo, visto que o nome aparece.

### 5) Defesa e Contra-ataque

- O jogador que recebe o ataque, pode escolher entre defender e contra-atacar, ele saberá apenas a vida e o nome de quem está atacando (a intenção é que o único parametro a ser analisado seja a precisão do oponente e o resto uma estratégia baseada em "sorte").

  - Defesa: O jogador pode reduzir o dano recebido. Um valor aleatório entre 0 e 50% da Defesa do lutador determinará o quanto do ataque será absorvido. Mesmo que o valor aleatório seja 0, há uma redução mínima de 1 ponto de dano.

  - Contra-ataque:  O lutador que irá receber o ataque terá 50% de chance de revidar (causar dano sem receber dano) e 50% de chance de tomar dano e não atacar no próximo turno.

> O valor da defesa é negativo, pois é somado ao valor de ataque para reduzi-ló, e nas situações onde a defesa súpera o dano de ataque, o valor da defesa ficára igual ao ataque apenas para melhor visual.

### 6) Fim do jogo

- Um dos times teve todos seus lutadores mortos, ou seja, a soma da vida de todos os lutadores da equipe chega a 0.

> Para isso utilizei uma variável global com a soma da vida de todos os lutadores.