# Input de dados

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade,")
elif idade >= 12:
    print("Você é um adolescente,")
else:
    print("Você é maior de idade,")

mensagem = "entrada autorizada." if idade >= 18 else "entrada não autorizada."
print(mensagem)