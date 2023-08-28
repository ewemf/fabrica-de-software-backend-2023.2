# crie um programa que leia o nome de tres pessoas: João Maia, João Abrantes e Pedro. Para os respectivos nomes imprima:'oi eu sou joao maia', 'oi eu sou joao abrantes', 'oi eu sou pedro', e caso o nome nao seja nenhum dos tres imprima 'oi meu nome é {nome}' 


# PRECISO TERMINAR AINDA
nome1 = input('Digite um nome: ')
nome2 = input('Digite outro nome: ')
nome3 = input('Digite mais um nome: ')

if nome1 == ('João Maia') or nome2 == ('João Maia') or nome3 == ('João Maia'):
    print('Oi, eu sou o João Maia.')
elif nome1 == ('João Abrantes') or nome2 == ('João Abrantes') or nome3 == ('João Abrantes'):
    print('Oi, eu sou o João Abrantes.')
elif nome1 == ('Pedro') or nome2 == ('Pedro') or nome3 == ('Pedro'):
    print('Oi, eu sou o Pedro.')
elif nome1 != ('João Maia'):
    print('Oi, meu nome é {}'.format(nome1))
    print('Oi, meu nome é {}'.format(nome2))
    print('Oi, meu nome é {}'.format(nome3))