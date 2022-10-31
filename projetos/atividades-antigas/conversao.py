cont = 0

for z in range(0, 100):
    op = int(input('Bem vindo ao conversor de valores, selecione uma opção abaixo: \n[ 1 ] Binário \n[ 2 ] Octal \n[ 3 ] Hexadecimal\nR: '))
    while op < 1 or op > 3:
        op = int(input('Número inválido, selecione novamente: \n[ 1 ] Binário \n[ 2 ] Octal \n[ 3 ] Hexadecimal\nR: '))
    valor = int(input('Digite o número INTEIRO que deseja transformar: '))
    if op == 1:
        valor2 = bin(valor)
        print('{} equivale a {} em Binário.'.format(valor, valor2))
    elif op == 2:
        valor2 = oct(valor)
        print('{} equivale a {} em Octal.'.format(valor, valor2))
    elif op == 3:
        valor2 = hex(valor)
        print('{} equivale a {} em Hexadecimal.'.format(valor, valor2))
    x = input('\nDeseja converter novamente(S ou N)?: ')
    if x == 'S':
        cont += 1
    elif x == 'N':
        print('Fim do pograma.')
        break