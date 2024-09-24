# Um dicionário é uma estrutura de dados que armazena pares de chave, permitindo acessar valores através de suas chaves

# Dicionario
pessoa = {"nome": "Igor", "idade": 30, "cidade": "São Paulo"}
print("dicionario de exempplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Alterando um valor
pessoa["sobrenome"] = "Damião"
print("Sobrenome:", pessoa["sobrenome"])
print("dicionario de exempplo:", pessoa)

# Alterando um valor existente
pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

# Remover um par de chave e valor
del pessoa["sobrenome"]
print("dicionario de exempplo:", pessoa)

# Metodos: keys(), values(), items()

# Método keys
chaves = list(pessoa.keys())
print("Chaves do dicionario:", chaves)
print("Primeira chave:", chaves[0])

# Método  values
valores = list(pessoa.values())
print("Valores do dicionários:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Método items
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeiro valor:", itens[0][1])
print("Primeiro chave-valor: %s = %s" %  (itens[0][0], itens[0][1]))