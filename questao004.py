#Implemente um jogo onde o computador escolhe um número aleatório entre 1 e 100, e o usuário tenta adivinhar. 
# Utilize um loop para permitir que o usuário faça várias tentativas, fornecendo dicas (maior ou menor) a cada tentativa.

import random

numero_secreto = random.randint(1, 100)

print('Bem-vindo ao jogo de adivinhação!')
print('Tente adivinhar o número entre 1 e 100.\n')

tentativa = None
while tentativa != numero_secreto:
    tentativa = int(input('Digite seu palpite: '))
    
    if tentativa < numero_secreto:
        print('Tente um número maior.')
    elif tentativa > numero_secreto:
        print('Tente um número menor.')
    else:
        print(f'Parabéns! Você acertou, o número era {numero_secreto}.')


