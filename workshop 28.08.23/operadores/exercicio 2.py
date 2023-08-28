# crie um programa que leia dois numeros e exiba a soma dos dois numeros, a subtracao, multiplicacao e divisao

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1/num2

print('Soma: {}; Subtração: {}; Multiplicação: {}; Divisão: {};'.format(soma, sub, mult, div))