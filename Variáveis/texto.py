# Uma string é uma sequência de caracteres usada para representar texto
nome_completo = "Igor Damião"

nome_completo_aspas = """Igor 
Damião"""

nome_completo_quebra = "Igor \
Damião"

nome = "Igor"
sobrenome = "Damião"

# formatacao
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + nome , sobrenome)
print("Nome completo (4a forma):", nome_completo_aspas)
print("Nome completo (5a forma):", nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (7a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (8a forma): {nome} {sobrenome}")
print("Nome completo (9a forma): {} {}".format(nome, sobrenome))

