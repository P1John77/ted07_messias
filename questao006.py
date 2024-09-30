# Crie um programa que peça ao usuário um número inteiro e 
# verifique se ele é primo. utilize um loop para testar a
# divisibilidade do numero por outros numeros menores>

if __name__=='__main__':
     
     n = int(input('Digite o numero desejado:'))
     e_primo = True

     for i in range(n, 0, -1):
          
        if (n % i) == 0:
            if n > 1 and i != n and i != 1:
                e_primo = False

     print(f'O numero {n} é primo? {e_primo}')            