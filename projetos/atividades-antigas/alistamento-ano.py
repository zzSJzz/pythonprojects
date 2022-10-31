import datetime
import os
cont = 0

for z in range(0, 100):
    x = int(input('Informe seu ano de nascimento: '))
    data = datetime.date.today()
    dia_atual = data.year
    idade = dia_atual - x
    data = idade - 17
    if data < 0:
        data2 = 17 - idade
    if idade < 17:
        print('Ainda faltam {} anos para você se alistar.'.format(data2))
    elif idade == 17:
        print('Parabéns! Você está no ano de alistamento, vá até a Junta mais próxima para mais informações.')
    else:
        print('Você já passou do período de alistamento em {} anos.'.format(data))
    x = input('\nDeseja consultar novamente(S ou N)?: ')
    if x == 'S':
            os.system('clear')
            cont += 1
    elif x == 'N':
            print('Fim do pograma.')
            break