#Desenvolva um programa que converta um número decimal fornecido pelo usuário para sua representação binária. 
# Utilize um loop para realizar as divisões sucessivas por 2 e armazenar os restos.

numero_decimal = int(input('Digite um número decimal para converter em binário: '))

if numero_decimal == 0:
    print('O número binário é 0.')
else:
    restos = []

    while numero_decimal > 0:
        restos.append(numero_decimal % 2) 
        numero_decimal //= 2  

    restos.reverse()

    numero_binario = ''.join(map(str, restos))

    print(f'A representação binária é: {numero_binario}')

