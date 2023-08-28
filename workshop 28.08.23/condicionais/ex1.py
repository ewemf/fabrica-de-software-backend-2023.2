# crie um programa que receba uma idade e retorne se pode obter carteira de motorista(CNH)

idade = int(input('Digite uma idade: '))

if idade >= 18:
    print('Pode obter a Carteira de motorista (CNH).')
else:
    print('NÃO pode obter a Carteira de motorista (CNH).')