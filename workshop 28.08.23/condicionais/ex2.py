# crie um programa que leia uma velocidade de um carro e multe se passar com velocidade maior que 80km/h. mostre que ele foi multado. a multa é de 7R$ por cada km acima do limite

velocidade = int(input('Digite a velocidade do carro em km/h: '))

multa = (velocidade - 80)*7

if velocidade > 80:
    print('Passou da velocidade máxima de 80km/h. MULTADO em R${}.'.format(multa))
else:
    print('O carro não ultrapassou a velocidade máxima de 80km/h.')