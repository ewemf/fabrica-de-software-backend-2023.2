#utilize estrutura de repeticao for para fazer a tabuada de adição de 0 a 10 de um numero digitado no terminal.

num = int(input("Digite um número: "))

for i in range(11):
    total = num + i
    print("{} + {} = {}".format(num, i, total))