#Crie um programa que peça ao usuário para inserir várias notas de um aluno e calcule a média
#Utilize um loop para continuar pedindo notas até que o usuário digite um valor específico para encerrar a entrada (por exemplo, -1).

notas = []
while True:
    nota = float(input('Insira a nota do aluno (ou digite -1 para encerrar): '))
    
    if nota == -1:
        break
    
    notas.append(nota)

if notas:
    media = sum(notas) / len(notas)
    print(f'A média do aluno é: {media:.2f}')
else:
    print('Nenhuma nota foi inserida.')
