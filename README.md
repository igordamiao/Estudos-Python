### Fundamentos de Python
![image](https://github.com/user-attachments/assets/00087e55-2fd9-4d84-b88b-0ed1adc4b8c6)

Este repositório contém exemplos e explicações dos principais fundamentos da linguagem Python. Ele foi criado para ajudar iniciantes e desenvolvedores a entender os conceitos básicos e aplicar Python de maneira eficiente.

**Conteúdo**
1. [Variáveis](#variaveis)
2. [Tipos de Dados](#tipos-de-dados)
  * Inteiros
  * Float
  * Strings
  * Listas
  * Tuplas
  * Dicionários
  * Booleanos

3. [Condicionais](#condicionais)
  * if, elif, else
4. [Laços de Repetição](#lacos-de-repeticao)
  * for
  * while
5. [Funções](#funcoes)
6. [Módulos e Pacotes](#modulos-e-pacotes)

## Variaveis
> Em Python, variáveis são usadas para armazenar dados. Não é necessário declarar o tipo de variável, pois Python é uma linguagem de tipagem dinâmica.

```python
x = 10
nome = "Python"
```

## Tipos de Dados
> Python possui vários tipos de dados nativos que podem ser usados para armazenar diferentes tipos de informação.

*Inteiros*
> Números inteiros, como 1, 100, -5.

```python
idade = 25
```

*Float*
> Números de ponto flutuante, como 3.14, -0.5.

```python
preco = 19.99
```

*Strings*
> Sequências de caracteres representadas por aspas simples ou duplas.

```python
nome = "Python"
```

*Listas*
> Estruturas mutáveis que armazenam uma sequência de elementos.

```python
frutas = ["maçã", "banana", "laranja"]
```

*Tuplas*
> Estruturas imutáveis que armazenam uma sequência de elementos.

```python
cores = ("vermelho", "azul", "verde")
```

*Dicionários*
> Estruturas de dados que armazenam pares chave.

```python
pessoa = {"nome": "João", "idade": 30}
```

*Booleanos*
>Valores lógicos: True ou False.

```python
ativo = True
```

## Condicionais
Condicionais são usadas para executar diferentes blocos de código com base em uma condição.

```python
if x > 10:
    print("Maior que 10")
elif x == 10:
    print("Igual a 10")
else:
    print("Menor que 10")
```

## Lacos de Repeticao
>Laços de repetição permitem executar blocos de código várias vezes.

*for*
>Usado para iterar sobre sequências como listas e strings.

```python
for fruta in frutas:
    print(fruta)
```

*while*
> Executa o bloco de código enquanto a condição for verdadeira.

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

## Funcoes
> Funções são blocos de código reutilizáveis que realizam uma tarefa específica.

```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Python")
```

## Modulos e pacotes
> Módulos são arquivos Python que contêm definições e implementações de funções e variáveis. Pacotes são coleções de módulos.

```python
import math

print(math.sqrt(16))  # Usa a função sqrt do módulo math
```

**Como usar este repositório**
1. Clone o repositório:

```python
git clone https://github.com/usuario/fundamentos-python.git
```

2. Acesse a pasta do projeto:

```python
cd fundamentos-python
```

3. Execute os exemplos Python:

```python
python exemplo.py
```

***Contribuindo***
> Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

***Licença***
> Este projeto está licenciado sob a [MIT licensed](https://github.com/nestjs/nest/blob/master/LICENSE).

