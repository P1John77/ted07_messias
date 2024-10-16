# Implemente um programa que simule o lançamento de um dado de 6 faces várias vezes, conforme especificado pelo usuário. 
# Utilize um loop para realizar os lançamentos e exibir os resultados.

import random

num_lancamentos = int(input('Quantas vezes você gostaria de lançar o dado? '))

print(f'\nLançando o dado {num_lancamentos} vezes...\n')

for i in range(1, num_lancamentos + 1):
    resultado = random.randint(1, 6)
    print(f'Lançamento {i}: {resultado}')

print('\nSimulação concluída!')

