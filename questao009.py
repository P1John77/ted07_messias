#Crie um programa que desenhe padrões simples com caracteres, como triângulos, quadrados ou losangos. 
# Utilize loops aninhados para controlar a quantidade de linhas e colunas e a exibição dos caracteres.

def desenhar_triangulo(altura):
    print('\nTriângulo:')
    for i in range(1, altura + 1):
        for j in range(i):
            print('*', end='')
        print()

def desenhar_quadrado(tamanho):
    print('\nQuadrado:')
    for i in range(tamanho):
        for j in range(tamanho):
            print('*', end='')
        print()

def desenhar_losango(tamanho):
    print('\nLosango:')
    for i in range(1, tamanho + 1):
        for j in range(tamanho - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print('*', end='')
        print()
    
    for i in range(tamanho - 1, 0, -1):
        for j in range(tamanho - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print('*', end='')
        print()

tamanho = int(input("Digite o tamanho para desenhar os padrões (por exemplo, 5): "))

desenhar_triangulo(tamanho)
desenhar_quadrado(tamanho)
desenhar_losango(tamanho)

