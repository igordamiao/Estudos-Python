# Uma tupla é uma estrutura de dados que armazena uma sequência ordenada e imutável de elementos.

# tupla de exemplo 
minha_tupla = (1, 2, 3, 4,)

print("Minha tupla:", minha_tupla)

print(minha_tupla[0])
print(minha_tupla[2])
print(minha_tupla[-1])


# Metodo count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece", contagem)

indice = minha_tupla.index(3)
print("Indice da primeira ocorrencia do elemento 3:", indice)