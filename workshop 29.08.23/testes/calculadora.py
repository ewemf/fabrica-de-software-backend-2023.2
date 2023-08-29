def calculadora ():
    def soma (a,b):
        print (a+b)
    def sub(a,b):
        print (a-b)
    def mult(a,b):
        print (a*b)
    def div(a,b):
        print (a/b)
    opcao = input('Digite a operação da calculadora: ')
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    if opcao == 'soma' or opcao == 'SOMA' or opcao == 'Soma':
        soma(num1, num2)
    elif opcao == 'subtração' or opcao == 'SUBTRAÇÃO' or opcao == 'Subtração':
        sub(num1, num2)
    elif opcao == 'multiplicação' or opcao == 'Multiplicação' or opcao == 'MULTIPLICAÇÃO':
        mult(num1, num2)
    elif opcao == 'divisão' or opcao == 'Divisão' or opcao == 'DIVISÃO':
        div(num1, num2)
    else:
        print('não reconhecido.')


calculadora()
