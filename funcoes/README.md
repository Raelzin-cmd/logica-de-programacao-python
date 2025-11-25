# Função

Uma função é um bloco de código reutilizável que executa uma tarefa específica.

Imagine que você tem que fazer a mesma coisa várias vezes. Em vez de repetir o mesmo processo manualmente, você cria uma função e deixa ela fazer isso para você.

Em resumo, uma função serve para:

- Evitar repetição de código.
- Organizar melhor seu programa.
- Dividir tarefas complexas em partes menores.
- Tornar tudo mais fácil de entender e modificar.

Sempre que você perceber que está repetindo um processo, ou que uma parte do seu código representa uma "tarefa" clara, você constrói uma função.

Exemplo prático em [funcoes.py](../funcoes/funcoes.py)

## Parâmetros

Parâmetros são como espaços reservados dentro da função.

Eles representam os dados que a função precisa para funcionar, mas que só serão conhecidos quando você realmente usar a função.

Ex: Se a função é uma máquina que faz suco, o "fruto" seria um parâmetro -- a máquina precisa saber qual fruta usar, mas você só coloca a fruta quando for usar.

Em resumo:

- O parâmetro é um "nome" dentro da função.
- Ele indica que a função precisa daquele dado para funcionar.
- Ele é definido dentro da criação da função, não quando ela é usada.

Exemplo prático em [funcoes-parametro.py](../funcoes/funcoes-parametro.py)

## Argumentos

Argumentos são os valores reais que você entrega para a função no momento em que a usa.

Voltando à máquina de suco: O parâmetro é “fruta”, mas o argumento é “laranja”, “maçã”, “uva” etc.

Em resumo:

- Argumento é o valor que preenche o parâmetro.
- Ele é passado no momento em que chamamos a função.
- Ele é o dado concreto com o qual a função realmente trabalha.

### Argumento Posicional 

Os argumentos e os parâmetros devem seguir a mesma ordem para não gerar conflito.

```python
def usuario(nome, idade, altura):

usuario('Rael', 26, 1.74)
```

### Argumento Nomeados

Os parâmetros recebem os valores dos argumentos que são nomeados igualmente. A ordem não importa.

```python
def usuario(nome, idade, altura):

usuario(idade = 26, altura = 1.74, nome = 'Rael')
```

## Quando usar o Return

`return` é a forma de uma função devolver um resultado.

Imagine que a função não só faz uma tarefa, mas também produz algo, como uma máquina que transforma matéria-prima em produto — ela processa algo e devolve o resultado para você.

O return serve para isso:

- Entregar de volta um valor.
- Permitir que esse valor seja guardado, usado, modificado ou enviado para outro lugar no programa.
- Finalizar a função (nada depois do return é executado).

Use return quando sua função:

- Precisa produzir um resultado.
- Calcula algo.
- Verifica algo e precisa informar essa verificação.
- Constrói alguma informação.
- Transforma dados e devolve a transformação.

NÃO use return quando a função:

- Apenas executa uma ação.
- Apenas mostra algo na tela.
- Faz uma tarefa que não precisa gerar um resultado para ser usado em outro lugar.

# Simples de Memorizar

- **Função** = a tarefa organizada.
- **Parâmetro** = o que a função precisa para funcionar.
- **Argumento** = o valor real que você dá para a função.
- **Return** = o resultado que a função te devolve.