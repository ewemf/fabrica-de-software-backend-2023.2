# crie um programa que receba uma quantidade de canetas pretas e azuis. A caneta azul vale R$2.00, a caneta preta vale R$2.50. Mostre a quantidade final a ser paga.

preta = int(input('Digite a quantidade de canetas PRETAS: '))
azul = int(input('Digite a quantidade de canetas AZUIS: '))

preta = preta * 2
azul = azul * 2.50

total = preta + azul

print('O valor total a ser pago é: R${}.'.format(total))