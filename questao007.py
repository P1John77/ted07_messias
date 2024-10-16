# Implemente um programa que calcule o fatorial de um número fornecido pelo usuário. 
# Utilize um loop para realizar as multiplicações necessárias.

numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1

if numero < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
else:
    for i in range(1, numero + 1):
        fatorial *= i
    
    print(f"O fatorial de {numero} é {fatorial}.")
