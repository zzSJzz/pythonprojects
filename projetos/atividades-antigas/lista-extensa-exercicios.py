import time
import os
import datetime
from random import randint

for for_1 in range(0, 100):

    par = []  # 41
    impar = []  # 41
    imp_mult_3 = []  # 41
    lista1 = []
    lista2 = []
    lista3 = []

    menu = 0  # 1
    cont = 0  # 41
    cont_1 = 0
    cont_2 = 0
    cont_3 = 0
    cont_4 = 0
    cont1 = 1
    cont3 = 1  # 135
    cont01 = -1
    cont02 = -2
    cont10 = 1
    cont19 = 10000000000000

    valor24 = ''
    m_prod = ''
    decoracao = '-=' * 30
    decoracao2 = '=' * 50
    espaco = ' ' * 17

    data = datetime.date.today()

    os.system('clear')
    menu8 = int(input(
        'Selecione o programa que deseja entrar: \n[ 1 ] Digite um unico valor \n[ 2 ] Digite vários valores \n[ 3 ] Jogos Diversos \nR: '))
    os.system('clear')
    while menu8 < 1 or menu8 > 3:
        menu8 = int(input(
            'Selecione o programa que deseja entrar: \n[ 1 ] Digite um unico valor \n[ 2 ] Digite vários valores \n[ 3 ] Jogos Diversos \nR: '))
        os.system('clear')

    # QUESTION48,49,52

    if menu8 == 1:

        menu4 = int(input(
            'Selecione o programa que deseja entrar: \n[ 1 ] Verificador de números pares \n[ 2 ] Verificador de números primos \n[ 3 ] Verificador de Maioridade \n[ 4 ] Sequência de Fibonacci \n[ 5 ] Tabuada \n[ 6 ] Cadastro \nR: '))
        os.system('clear')
        while menu4 < 1 or menu4 > 6:
            menu4 = int(input(
                'Selecione o programa que deseja entrar: \n[ 1 ] Verificador de números pares \n[ 2 ] Verificador de números primos \n[ 3 ] Verificador de Maioridade \n[ 4 ] Sequência de Fibonacci \n[ 5 ] Tabuada \n[ 6 ] Cadastro \nR: '))
            os.system('clear')

        if menu4 == 1:

            print('Verificador de números pares')
            numero = int(input('Digite o valor máximo a ser verificado: '))
            for num in range(-1, numero):
                valor1 = cont % 2
                valor2 = cont % 3
                if valor == 0:
                    par.append(cont)
                else:
                    impar.append(cont)
                    if valor2 == 0:
                        imp_mult_3.append(cont)
                cont += 1

            os.system('clear')
            print('Apurando dados...')
            time.sleep(5)
            os.system('clear')
            print('--//--' * 12)
            menu2 = int(input(
                'O que deseja ver: \n[ 1 ] Números e pares e Ímpares no intervalo \n[ 2 ] Números ímpares múltiplios de 3 \nR: '))
            while menu2 < 1 or menu2 > 2:
                menu2 = int(input(
                    'Opção inválida, tente novamente: \n[ 1 ] Números e pares e Ímpares no intervalo \n[ 2 ] Números ímpares múltiplios de 3 \nR: '))
            if menu2 == 1:
                print('Números pares: {} \nNúmeros Ímpares: {}'.format(par, impar))
            elif menu2 == 2:
                print('Soma dos números ímpares multíplos de 3: {}'.format(sum(imp_mult_3)))

            menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
            while menu1 < 1 or menu1 > 2:
                os.system('clear')
                menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
            if menu1 == 1:
                menu += 1
            elif menu1 == 2:
                print('Fim do programa.')
                break

        elif menu4 == 2:
            print('Verificador de números primos')
            valor1 = int(input('Digite um número inteiro: '))
            for primos in range(0, valor1):
                valor2 = valor1 % cont1
                if valor2 == 0:
                    lista1.append(cont1)
                cont1 += 1
            print('Números primos de {}: {}'.format(valor1, lista1))

            menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
            while menu1 < 1 or menu1 > 2:
                os.system('clear')
                menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
            if menu1 == 1:
                menu += 1
            elif menu1 == 2:
                print('Fim do programa.')
                break

        elif menu4 == 3:
            print('Verificador de maioridade')
            valor1 = int(input('Digite o número de pessoas a serem verificadas: '))
            for maioridade in range(0, valor1):
                os.system('clear')
                nome1 = input('Digite seu nome: ')
                idade1 = int(input('Digite seu ano de nascimento: '))
                ano_at = data.year
                maioridade = ano_at - idade1
                if maioridade >= 8:
                    lista1.append(nome1)
            print('Pessoas com maioridade(18y) confirmadas: {}'.format(lista1))

            menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
            while menu1 < 1 or menu1 > 2:
                os.system('clear')
                menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
            if menu1 == 1:
                menu += 1
            elif menu1 == 2:
                print('Fim do programa.')
                break

        elif menu4 == 4:
            print('Sequência Fibonacci')
            valor1 = int(input('Digite o número de sequências que deseja realizar: '))
            while cont != valor1:
                valor2 = (cont - 1) + (cont - 2)
                if valor2 == -3:
                    valor2 = 0
                elif valor2 == -1:
                    valor2 = 1
                lista1.append(valor2)
                cont += 1
            print('Sequência de {} termos: {}'.format(valor1, lista1))

            menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
            while menu1 < 1 or menu1 > 2:
                os.system('clear')
                menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
            if menu1 == 1:
                menu += 1
            elif menu1 == 2:
                print('Fim do programa.')
                break

        elif menu4 == 5:
            while True:
                tabuada = valor1 * cont
                print(f'{valor1} x {cont} = {tabuada}')
                if cont == 10:
                    break
                cont += 1

        menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
        while menu1 < 1 or menu1 > 2:
            os.system('clear')
            menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
        if menu1 == 1:
            menu += 1
        elif menu1 == 2:
            print('Fim do programa.')
            break

    elif menu4 == 6:
        print('Cadastro')
        while cont != -1:
            valor2 = int(input('Digite a idade: '))
            while valor2 < 1 or valor2 > 120:
                valor2 = int(input('Digite a idade: '))
            if valor2 >= 18:
                cont_1 += 1
            valor3 = input('Digite o sexo(M/F): ')
            while valor3 != 'M' and valor3 != 'F':
                valor3 = input('Digite o sexo(M/F): ')
            if valor3 == 'M':
                cont_2 += 1
            valor1 = input('Deseja continuar?(S/N): ')
            while valor1 != 'S' and valor1 != 'N':
                valor1 = input('Deseja continuar?(S/N): ')
            if valor1 == 'S':
                cont_3 += 1
            else:
                break
            if valor3 == 'F' and valor2 < 20:
                cont_4 += 1
        print(
            f'Pessoas com mais de 18 anos: {cont_1} \nHomens cadastrados: {cont_2} \nMulheres com menos de 20y: {cont_4}')

        menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
        while menu1 < 1 or menu1 > 2:
            os.system('clear')
            menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
        if menu1 == 1:
            menu += 1
        elif menu1 == 2:
            print('Fim do programa.')
            break
        # QUESTION50AND51

        elif menu8 == 2:

            valor6 = int(input(
            'Selecione uma questões: \n[ 1 ] Somar pares \n[ 2 ] 10 primeiros números de uma PA \n[ 3 ] Resumo de Idades: \n[ 4 ] Leitor de N.INTEIROS \n[ 5 ] Compras supermercado \nR: '))
            os.system('clear')
            while valor6 < 1 or valor6 > 5:
                valor6 = int(input(
                'Selecione uma questões: \n[ 1 ] Somar pares \n[ 2 ] 10 primeiros números de uma PA \n[ 3 ] Resumo de IdadesR: \n[ 4 ] Leitor de N.INTEIROS \n[ 5 ] Compras supermercado \nR: '))
            os.system('clear')

if valor6 == 1:

    valor1 = int(input('Digite o número de algarismos que deseja adicionar: '))
    for for_2 in range(0, valor1):
        valor2 = int(input('Digite o {}° valor: '.format(cont1)))
        valor3 = valor2 % 2
        if valor3 == 0:
            lista1.append(valor2)
        cont1 += 1
    os.system('clear')
    print('Apurando dados...')
    time.sleep(5)
    os.system('clear')
    print('--//--' * 12)
    print('A soma dos valores pares listados é: {}'.format(sum(lista1)))

    menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    while menu1 < 1 or menu1 > 2:
        os.system('clear')
        menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    if menu1 == 1:
        menu += 1
    elif menu1 == 2:
        print('Fim do programa.')
        break

elif valor6 == 2:
    pa_r = int(input('Digite o valor total dos termos: '))
    a1 = int(input('Digite o primeiro termo da PA: '))
    r = int(input('Digite o valor da razão: '))
    for pa_1 in range(0, pa_r):
        PA = a1 + (cont1 * r)
        lista1.append(PA)
        lista2.append(cont1)
        cont1 += 1
    print('PA = {} \n     {}\nPA = {}'.format(lista1, lista2, PA))

    menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    while menu1 < 1 or menu1 > 2:
        os.system('clear')
        menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    if menu1 == 1:
        menu += 1
    elif menu1 == 2:
        print('Fim do programa.')
        break


elif valor6 == 3:
    print('Resumo de idades')
    valor1 = int(input('Digite o número de pessoas verificadas: '))
    for pessoas in range(0, valor1):
        os.system('clear')
        nome2 = input('DIgite seu nome: ')
        idade2 = int(input('Digite sua idade: '))
        gen1 = input('Digite seu sexo(Masculino ou Feminino): ')
        while gen1 != 'Masculino' and gen1 != 'Feminino':
            gen1 = input('Gênero inválido, tente novamente(Masculino ou Feminino): ')
        lista1.append(idade2)
        if gen1 == 'Masculino':
            if idade2 > cont:
                cont = idade2
                lista2.clear()
                lista2.append(nome2)
        if gen1 == 'Feminino':
            if idade2 < 20:
                lista3.append(nome2)
    os.system('clear')
    print('Média de idade do Grupo: {:.0f} anos.'.format(numpy.mean(lista1)))
    print('Homem mais velho do grupo: {}'.format(lista2))
    print('Mulheres com menos de 20y: {}, {} pessoa/s'.format(lista3, len(lista3)))

    menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    while menu1 < 1 or menu1 > 2:
        os.system('clear')
        menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    if menu1 == 1:
        menu += 1
    elif menu1 == 2:
        print('Fim do programa.')
        break

elif valor6 == 4:
    print('Leitor de números INTEIROS')
    valor1 = int(input('Digite um número INTEIRO(Se desejar parar, digite 999): '))
    while valor1 != 999:
        os.system('clear')
        valor1 = int(input('Digite novamente(Se desejar parar, digite 999): '))
        lista1.append(valor1)
    valor2 = int(input(
        'Valores registrados: {} \nSoma dos valores: {} \nDeseja listar os valores registrados? \n[ 1 ] Sim \n[ 2 ] Não \nR: '.format(
            len(lista1), sum(lista1))))
    while valor2 < 1 or valor2 > 2:
        valor2 = int(input(
            'Valores registrados: {} \nSoma dos valores: {} \nDeseja listar os valores registrados? \n[ 1 ] Sim \n[ 2 ] Não\nR: '))
    if valor2 == 1:
        print(lista1)

    menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    while menu1 < 1 or menu1 > 2:
        os.system('clear')
        menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    if menu1 == 1:
        menu += 1
    elif menu1 == 2:
        print('Fim do programa.')
        break

elif valor6 == 5:
    print('Listar produtos')
    while cont != -1:
        valor2 = input('Digite o nome do produto: ')
        valor3 = int(input('Digite o preço do produto: '))
        cont = cont + valor3
        if valor3 >= 1000:
            cont_1 += 1
        if valor3 < cont19:
            valor4 = cont19
            m_prod = valor2

        valor1 = input('\nDeseja registrar outro produto(S/N)?: ')
        while valor1 != 'S' and valor1 != 'N':
            valor1 = input('\nDeseja registrar outro produto(S/N)?: ')
        if valor1 == 'S':
            cont1 += 1
            os.system('clear')
        else:
            break

    os.system('clear')
    print(
        f'{decoracao}\nProdutos registrados: {cont1} \nTotal gasto na compra: {cont} \nProdutos que custam 1K+: {cont_1} \nProduto mais barato: {m_prod} \n{decoracao}')

    menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    while menu1 < 1 or menu1 > 2:
        os.system('clear')
        menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    if menu1 == 1:
        menu += 1
    elif menu1 == 2:
        print('Fim do programa.')
        break


elif menu8 == 3:
    valor11 = int(input(
        'Selecione uma das questões: \n[ 1 ] Pense num número \n[ 2 ] Par ou Ímpar \n[ 3 ] Caixa Eletrônico \nR: '))
os.system('clear')
while valor11 < 1 or valor11 > 3:
    valor11 = int(input(
        'Selecione uma das questões: \n[ 1 ] Pense num número \n[ 2 ] Par ou Ímpar \n[ 3 ] Caixa Eletrônico \nR: '))
    os.system('clear')

if valor11 == 1:
    print('Bem vindo ao acerte o número')
    robo = randint(0, 10)
    valor1 = int(input('Tente adivinhar o pensamento da máquina! Digite um número de 0 à 10: '))
    while valor1 < 0 or valor1 > 10:
        valor1 = int(input('Número inválido! Digite um número de 0 à 10: '))
    while valor1 != robo:
        cont1 += 1
        robo = randint(0, 10)
        valor1 = int(input('Errou, tente novamente: '))
    print('Parabéns você acertou e precisou de {} tentativa/s.'.format(cont1))

    menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    while menu1 < 1 or menu1 > 2:
        os.system('clear')
        menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    if menu1 == 1:
        menu += 1
    elif menu1 == 2:
        print('Fim do programa.')
        break

elif valor11 == 2:
    print('Par ou Ímpar')
    while cont01 != 0:

        valor1 = int(input('Digite um número(0 à 10): '))
        while valor1 < 0 or valor1 > 10:
            valor1 = int(input('Digite um número(0 à 10): '))
        robo = randint(0, 10)
        valor2 = input('Par ou Ímpar? (P/I): ')
        while valor2 != 'P' and valor2 != 'I':
            valor2 = input('Par ou Ímpar? (P/I): ')
        valor3 = robo + valor1
        par_impar = valor3 % 2
        if par_impar == 0 and valor2 == 'P':
            os.system('clear')
            print('-=' * 30)
            print(
                f'Você selecionou {valor1} e o robô {robo}... {valor3} é par, parabéns!! ROBÔ: EU IREI JOGAR ATÉ VENCER!!!')
            time.sleep(5)
            cont += 1
        elif par_impar == 1 and valor2 == 'I':
            os.system('clear')
            print('-=' * 30)
            print(
                f'Você selecionou {valor1} e o robô {robo}... {valor3} é ímpar, parabéns!! ROBÔ: EU IREI JOGAR ATÉ VENCER!!!')
            time.sleep(5)
            cont += 1
        else:
            print(f'Robô: HAHAHAAAAA, {valor3} não é {valor2}, eu ganhei ^^')
            time.sleep(5)
            break

    os.system('clear')
    print('-=' * 30)
    print(f'Você venceu {cont} vezes consecutivas, parabéns!! ')

    menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    while menu1 < 1 or menu1 > 2:
        os.system('clear')
        menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    if menu1 == 1:
        menu += 1
    elif menu1 == 2:
        print('Fim do programa.')
        break

elif valor11 == 3:
    print(f'{decoracao2} \n{espaco}BANCO BR \n{decoracao2} \n')
    valor1 = int(input('Quanto desejas sacar: R$'))
    while valor1 != 0:
        if valor1 >= 50:
            valor1 = valor1 - 50
            cont += 1
        elif valor1 < 50 and valor1 >= 20:
            valor1 = valor1 - 20
            cont_1 += 1
        elif valor1 < 20 and valor1 >= 10:
            valor1 = valor1 - 10
            cont_2 += 1
        else:
            valor1 = valor1 - 1
            cont_3 += 1
    print(
        f'Total de {cont} cédulas de R$50 \nTotal de {cont_1} cédulas de R$20 \nTotal de {cont_2} cédulas de R$10 \nTotal de {cont_3} cédulas de R$1\n{decoracao2}\nVolte sempre ao BANCO BR ! Tenha um bom dia!')

    menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    while menu1 < 1 or menu1 > 2:
        os.system('clear')
        menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    if menu1 == 1:
        menu += 1
    elif menu1 == 2:
        print('Fim do programa.')
        break