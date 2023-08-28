#utilizando estrutura de repeticao while crie um programa que faça a soma de todos os numeros digitados. o loop so devera parar quando for digitado 0

total = 0
num = float(input("Digite um número (ou 0 para encerrar): "))
while num != 0:
    total += num
    num = float(input("Digite um número (ou 0 para encerrar): "))
print("A soma dos números digitados é:", total)