# desenvolva um progama que gere os primeiros N numeros
# da sequencia de fibonaci
if __name__ == '__main__':
    
    n = int(input('Digite o numero desejado:'))

    fn1 = 0
    fn2 = 1
 
#utilize um loop para calcular e exibir os termos da sequencia.
    for i in range(n):
        resultado = fn1 + fn2
        fn1 = fn2
        fn2 = resultado


        print(f'Resultado: {resultado} | fn1 => {fn1} | fn2 => {fn2}')
