import os

menu = 0

for menu_rep in range(0, 100):
    os.system('clear')
    menu = int(
        input('Selecione o programa que deseja entrar: \n[ 1 ] 1 questão \n[ 2 ] 2 questão \n[ 3 ] 3 questão\nR: '))
    os.system('clear')
    while menu < 1 or menu > 3:
        menu = int(
            input('Selecione o programa que deseja entrar: \n[ 1 ] 1 questão \n[ 2 ] 2 questão \n[ 3 ] 3 questão\nR: '))
        os.system('clear')

    if menu == 1:
        salario = int(input('Digite seu salário: '))
        vendas = int(input('Digite suas vendas: '))
        comissao = vendas * 0.04
        sal_tot = salario + comissao
        print(f'Com {comissao} reais em comissões, seu salário total foi de {sal_tot} reais.')

    elif menu == 2:
        base = int(input('Informe o valor da base da casa: '))
        altura = int(input('Informe a altura da casa: '))
        area = (base * altura) / 2
        potencia = area * 18
        kw = potencia / 1000
        if potencia >= 1000:
            print(f'Com uma área de {area}m2 faz- se necessário {kw} Kilowatts de potência.')
        else:
            print(f'Com uma área de {area}m2 faz- se necessário {potencia} watts de potência.')
    menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))

    while menu1 < 1 or menu1 > 2:
        os.system('clear')
        menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    if menu1 == 1:
        menu += 1
    elif menu1 == 2:
        print('Fim do programa.')
        break