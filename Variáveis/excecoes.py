# Exceções são eventos que ocorrem durante a execução de um programa que interrompem o fluxo normal de execução.
print("Exemplo de captura de execeções")
try: 
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"Erro de value error: {e}")
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"Erro: {e}")
else:
    print(f"resultado: {resultado}")
finally:
    print("Operacao finalizada")