#Crie um programa que peça ao usuário uma frase e conte o número de vogais e consoantes presentes nela.
#Utilize um loop para percorrer cada caractere da frase e realizar a contagem.

frase = input('Digite uma frase: ').lower()

vogais = 'aeiou'

contador_vogais = 0
contador_consoantes = 0

for caractere in frase:
    if caractere.isalpha():
        if caractere in vogais:
            contador_vogais += 1
        else:
            contador_consoantes += 1

print(f'Número de vogais: {contador_vogais}')
print(f'Número de consoantes: {contador_consoantes}')

