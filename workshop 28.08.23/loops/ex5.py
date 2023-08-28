#utilizando estrutura de repeticao while crie um programa que peça varios nomes e só pare quando for digitado "parar"

nomes = []
nome = input("Digite um nome (ou 'parar' para encerrar): ")
while nome != "parar" and nome != "Parar" and nome != "PARAR":
    nomes.append(nome)
    nome = input("Digite um nome (ou 'parar' para encerrar): ")