# Módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser reutilizadas em outros arquivos Python
print("Exemplo de importação de um módulo padrão: ")
# import math // math.sqrt
# Import da função especifica (altamente recomendado)
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é: ", raiz_quadrada)


print("\nExemplo de criação de utilização de um módulo personalizado")
# import meu_modulo
from meu_modulo import saudacao, dobro
mensagem = saudacao("Igor")
print(f"\n{mensagem}")

resultado_dobro = dobro(5)
print(f"\nO dobro de 5 é {resultado_dobro}")