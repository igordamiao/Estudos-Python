# Condicionais são estruturas que permitem tomar decisões com base em uma expressão booleana (verdadeira ou falsa)

# if, elif e else 

# Exemplo com operador > e ==
idade = 19
print(idade)

if idade > 18:
    print("Entrada autorizada 1")
elif idade == 18:
    print("Entrada autorizada 2")
else: 
    print("Entrada não autorizada")

# Exemplo apenas com if e else com operador >=
if idade >= 18:
    print("Idade maior ou igual 18")
else: 
    print("Idade menor que 18")

# Exemplo apenas com if e else operador <
if idade < 18:
    print("Idade menor 18")
else: 
    print("Idade maior que 18")

# Exemplo apenas com if e else operador != (diferente)
if idade != 18:
    print("Idade diferente de 18")
else: 
    print("Idade igual a 18")