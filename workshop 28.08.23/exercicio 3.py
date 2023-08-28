# crie um programa que leia dois numeros e que exiba True se o primeiro numero for maior que o primeiro e False se o primeiro numero for menor ou igual ao segundo numero

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('TRUE.')
elif num1 <= num2:
    print('FALSE.')
else:
    print('INVÁLIDO.')