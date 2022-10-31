# imports
import os

while True:

    # varieble

    cont = 0
    cont1 = 1
    cont2 = 2

    tupla1 = ()
    tupla2 = ()

    lista1 = []
    lista2 = []

    espaco = '  ' * 15
    decoracao = '-=' * 30
    ass1 = '\n[ 1 ] Tupla \n[ 2 ] Lista\nR: '
    ass2 = '\n[ 1 ] Leitor de número \n[ 2 ] Tabela Brasileirão \nR: '
    ass3 = '\n[ 1 ] 5 valores na lista \n[ 2 ] REGISTRO DE VALORES \nR: '

    os.system('clear')
    print(f'{espaco}MENU \n{decoracao}')
    menu1 = int(input(f'selecione uma opção\: {ass1}'))
    while menu1 not in (1, 2):
        menu1 = int(input(f'selecione uma opção\: {ass1}'))

    if menu1 == 1:
        os.system('clear')
        print(f'{espaco}MENU \n{decoracao}')
        menu1 = int(input(f'selecione uma opção\: {ass2}'))
        while menu1 not in (1, 2):
            menu1 = int(input(f'selecione uma opção\: {ass2}'))

        if menu1 == 1:

            os.system('clear')
            print('Leitor de números')
            tupla1 = (
            'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
            valor1 = int(input('Digite um número entre 0 e 20: '))
            while valor1 not in range(0, 21):
                valor1 = int(input('Digite um número entre 0 e 20: '))
            print(f'{valor1} é {tupla1[valor1]} por extenso.')

            final = input('Deseja iniciar o programa novamente(S/N)? ').strip().upper()
            while final not in 'SN':
                final = input('Deseja iniciar o programa novamente(S/N)? ').strip().upper()
            if final == 'N':
                break

        elif menu1 == 2:
            os.system('clear')
            print('Tabela do Brasileirão')
            tupla1 = (
            'Cruzeiro', 'Bahia', 'Vasco', 'Sport', 'Grêmio', 'Criciúma', 'Tombense', 'Operário', 'Sampaio Corrêa',
            'Londrina', 'Chapecoense', 'CRB', 'Novorizontino', 'Brusque', 'Ituano', 'CSA', 'Ponte Preta', 'Náutico',
            'Guarani', 'Vila Nova')
            print(f'Os cincos primeiros colocados: {tupla1[0:4]} \nOs últimos 4 colocados: {tupla1[16:20]}')
            for cont in range(0, len(tupla1)):
                if tupla1[cont] == 'Chapecoense':
                    cont += 1
                    print(f'Posição na tabela do Chapecoense: {cont}° lugar.')

            final = input('Deseja iniciar o programa novamente(S/N)? ').strip().upper()
            while final not in 'SN':
                final = input('Deseja iniciar o programa novamente(S/N)? ').strip().upper()
            if final == 'N':
                break


    elif menu1 == 2:
        os.system('clear')
        print(f'{espaco}MENU \n{decoracao}')
        menu1 = int(input(f'selecione uma opção\: {ass3}'))
        while menu1 not in (1, 2):
            menu1 = int(input(f'selecione uma opção\: {ass3}'))

        if menu1 == 1:
            os.system('clear')
            print(f'{espaco}5 VALORES \n{decoracao}')
            for valores in range(0, 5):
                valor1 = int(input(f'Digite o {cont1}° número: '))
                cont1 += 1
                if valor1 == 0 or valor1 > len(lista2):
                    lista2.append(valor1)
                else:
                    while cont < len(lista2):
                        if valor1 <= lista2(cont):
                            lista2.insert(cont, valor1)
                            cont == 0
                        cont += 1
                lista1.append(valor1)
            valor2 = max(lista1)
            valor3 = min(lista1)

            print(
                f'Valores digitados {lista1} \nMaior valor: {valor2} foi digitado na posição {lista1.index(valor2)} \nMenor valor: {valor3} foi digitado na posição {lista1.index(valor3)}')

            final = input('Deseja iniciar o programa novamente(S/N)? ').strip().upper()
            while final not in 'SN':
                final = input('Deseja iniciar o programa novamente(S/N)? ').strip().upper()
            if final == 'N':
                break

        elif menu1 == 2:
            os.system('clear')
            print(f'{espaco}REGISTRO DE VALORES \n{decoracao}')
            while True:
                valor1 = int(input('Digite um valor: '))
                for cont in lista1:
                    while valor1 == cont:
                        valor1 = int(input('Este valor já está na lista, tente novamente: '))
                lista1.append(valor1)
                valor2 = input('Deseja digitar o valor novamente(S/N)? ').strip().upper()
                while valor2 not in 'SN':
                    valor2 = input('Resposta inválida, digite novamente(S/N)? ').strip().upper()
                if valor2 == 'N':
                    break
            print(f'{decoracao} \nNúmeros digitados: {sorted(lista1)}')

            final = input('Deseja iniciar o programa novamente(S/N)? ').strip().upper()
            while final not in 'SN':
                final = input('Deseja iniciar o programa novamente(S/N)? ').strip().upper()
            if final == 'N':
                break

print('Fim do programa')