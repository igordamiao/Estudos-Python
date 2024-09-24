# Uma função é um bloco de código reutilizável que realiza uma tarefa específica.

def saudacao(nome):
 print(f"Olá, {nome}!")

print("\n Chamando a função saudação:")
saudacao("Alice")
saudacao("Bobby")

# Função com retorno, quadrado de um número recebido
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\n Chamando a função quadrado:")
resultado_quadrado = quadrado(6)
print("Resultado da função quadrado", resultado_quadrado)

# Função com multiplos parametros
def soma(numero1, numero2):
   resultado = numero1 + numero2
   return resultado

print("\nChamando a função soma:")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("A soma do número %s + %s é %s" % (numero1, numero2, resultado_soma))