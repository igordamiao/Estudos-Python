# O laço for é uma estrutura de repetição que itera sobre uma sequência de elementos (como listas, strings, tuplas, dicionários ou objetos iteráveis)

#lista
print("\nFor utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

#tupla
print("\nFor utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

#dicionario
print("\nFor utilizando dicionario - chaves")
pessoa = {"nome": "Igor", "idade": 30, "cidade": "São Paulo"}
for chaves in pessoa.keys():
    print(chaves)

print("\nFor utilizando dicionario - valores")
pessoa = {"nome": "Igor", "idade": 30, "cidade": "São Paulo"}
for valores in pessoa.values():
    print(valores)

print("\nFor utilizando dicionario - chaves e valores")
pessoa = {"nome": "Igor", "idade": 30, "cidade": "São Paulo"}
for chaves, valores in pessoa.items():
    print(f"{chaves}: {valores}")

# range(): intervalo numérico [0,1,2,3,4,5,6,7,8,9,10]
print("\nFor utilizando range")
for numero in range(5):
    print("Numero:", numero)

# range + len
print("\nFor utilizando range + len")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

# enumerate()
lista_enumerate = ["a", "b", "c", "d", "e",]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")