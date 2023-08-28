# crie um programa que leia o nome de tres pessoas: João Maia, João Abrantes e Pedro. Para os respectivos nomes imprima:'oi eu sou joao maia', 'oi eu sou joao abrantes', 'oi eu sou pedro', e caso o nome nao seja nenhum dos tres imprima 'oi meu nome é {nome}' 

nome1 = input('Digite um nome: ')
nome2 = input('Digite outro nome: ')
nome3 = input('Digite mais um nome: ')

if nome1 == 'João Maia':
    print('Oi, eu sou João Maia.')
elif nome1 == 'João Abrantes':
    print('Oi, eu sou João Abrantes.')
elif nome1 == 'Pedro':
    print('Oi, eu sou Pedro.')
else:
    print('Oi, meu nome é', nome1)

if nome2 == 'João Maia':
    print('Oi, eu sou João Maia.')
elif nome2 == 'João Abrantes':
    print('Oi, eu sou João Abrantes.')
elif nome2 == 'Pedro':
    print('Oi, eu sou Pedro.')
else:
    print('Oi, meu nome é', nome2)

if nome3 == 'João Maia':
    print('Oi, eu sou João Maia.')
elif nome3 == 'João Abrantes':
    print('Oi, eu sou João Abrantes.')
elif nome3 == 'Pedro':
    print('Oi, eu sou Pedro.')
else:
    print('Oi, meu nome é', nome3)