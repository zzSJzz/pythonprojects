import random

cont = 1
lista = []
x = int(input('Digite o número de nomes(max: 10): '))
while cont <= x:
    n1 = str(input('\nDigite o {}° nome: '.format(cont)))
    cont += 1
    lista.append(n1)
    print(lista)

print('\nO nome sorteado foi: {}'.format(random.choice(lista)))
