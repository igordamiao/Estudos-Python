# Uma lista é uma estrutura de dados que armazena uma sequência ordenada de elementos, que podem ser de diferentes tipos de dados (inteiros, strings, outras listas, etc.)

# Declaracao 
minha_lista = [1, 2, 3, 4, 5, "texto", True, False]

# Exibindo lista
print("minha lista de exemplo", minha_lista)

# Mutacao
minha_lista[0] = "python"
print("Minha lista de exemplo", minha_lista)

# Exibindo elementos
print("minha_lista[0]:",minha_lista[0])
print("minha_lista[5]:",minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])
print("minha_lista[:6]:", minha_lista[:6])
print("minha_lista[2:]:", minha_lista[2:])

# Metodos de lista

# append(): Adiciona um elemento no final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# index(): retorna o indice do elemento
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# insert: insere um elemento em um indice especifico
minha_lista.insert(2, 10)
print("Após insert(2,10):",minha_lista)

# pop: remove e retorna o elemento de um indice especifico
elemento_removido = minha_lista.pop(3)
print("Elemento removido:",elemento_removido)
print("Após pop(3):", minha_lista)

# remove: remove o primeiro elemento com o valor especificado
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

# sort: ordena a lista em ordem crescente
minha_lista = [1, 6 , 4, 5, 3, 7, 8, 15, 2]
minha_lista.sort()
print("Após sort():", minha_lista)