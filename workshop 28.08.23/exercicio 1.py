# crie um programa que peça um numero e mostre o seu sucessor e antecessor

num = int(input('Digite um número: '))

antecessor = num - 1
sucessor = num + 1

print('O SUCESSOR do número escolhido é: {}; Já o ANTECESSOR do número escolhido é: {}'.format(sucessor, antecessor))