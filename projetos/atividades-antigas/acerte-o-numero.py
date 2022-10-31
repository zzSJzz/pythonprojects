from random import randint
cont = 0
namx = 100
for z in range(0, 100):
    print('Bem vindo ao "ACERTE O NÚMERO"')
    jogador = int(input('Tente acertar meu pensamento! Adivinhe um número de 0 a 5: '))
    while jogador < 0 or jogador > 5:
         jogador = int(input('Número inválido, tente novamente(0 a 5): '))
    robo = randint(0, 5)
    if robo == jogador:
        x = input('Acertou!! Deseja jogar novamente(S ou N)?: ')
        if x == 'S':
            cont += 1
        elif x == 'N':
            print('Fim do pograma.')
            break
    else:
        x = input('Errou, que pena!! Deseja jogar novamente(S ou N)?: ')
        if x == 'S':
            cont += 1
        elif x == 'N':
            print('Fim do pograma.')
            break