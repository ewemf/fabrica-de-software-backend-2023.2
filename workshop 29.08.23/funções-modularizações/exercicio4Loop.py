# crie um programa que receba uma quantidade de canetas pretas e azuis. A caneta azul vale R$2.00, a caneta preta vale R$2.50. Mostre a quantidade final a ser paga.
def total (p,a):
    return (p * 2) + (a * 2.50)

p = int(input('Digite a quantidade de canetas PRETAS: ')) #canetas pretas
a = int(input('Digite a quantidade de canetas AZUIS: ')) #canetas azuis

print('Preço do valor total: R${}'.format(total(p,a)))