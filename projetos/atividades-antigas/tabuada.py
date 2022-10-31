print('TABUADA\n')
cont = 1
x = int(input('Digite o algarismo desejado(1 até 9): '))

while x <= 0 or x >= 10:
    x = int(input('Algarismo inválido, digite novamente(1 até 9): '))

for y in range(0, 9):
    result = x * cont
    print('{} x {} = {}'.format(x, cont, result))
    cont += 1

