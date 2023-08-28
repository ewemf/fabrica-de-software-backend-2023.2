#utilizando estrutura de repeticao while crie um programa que leia exclusivamente o sexo como 'F' e 'M' e o loop so deve terminar quando sexo for = sair. ao fim mostre a quantidade e mulheres e homens

fem = 0
masc = 0

sexo = input("Digite o sexo (F/M) ou 'sair' para encerrar: ")
while sexo != "sair" and sexo != "Sair" and sexo != "SAIR":
    if sexo == "F":
        fem += 1
    elif sexo == "M":
        masc += 1
    sexo = input("Digite o sexo (F/M) ou 'sair' para encerrar: ")

print("Quantidade de mulheres:", fem)
print("Quantidade de homens:", masc)





