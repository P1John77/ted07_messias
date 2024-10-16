#Desenvolva um programa que peça ao usuário um número e gere a tabuada completa desse número (de 1 a 10).
#Utilize um loop para realizar as multiplicações e exibir os resultados de forma organizada.

numero = int(input("Digite um número para gerar a tabuada: "))

print(f"\nTabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

