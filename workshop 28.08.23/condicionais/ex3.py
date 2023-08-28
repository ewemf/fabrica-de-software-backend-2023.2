# crie um programa que leia tres numeros e mostre qual deles e o maior e o menor

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

if num1 > num2 and num1 > num3:
    print('{} É O MAIOR NÚMERO.'.format(str(num1)))
elif num2 > num1 and num2 > num3:
    print('{} É O MAIOR NÚMERO.'.format(str(num2)))
elif num3 > num1 and num3 > num2:
    print('{} É O MAIOR NÚMERO.'.format(str(num3)))


if num1 < num2 and num1 < num3:
    print('{} É O MENOR NÚMERO.'.format(str(num1)))
elif num2 < num1 and num2 < num3:
    print('{} É O MENOR NÚMERO.'.format(str(num2)))
elif num3 < num1 and num3 < num2:
    print('{} É O MENOR NÚMERO.'.format(str(num3)))