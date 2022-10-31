# Exemplo de menu para ser utilizado
import os

menu = 0

for menu_rep in range(0, 100):
    os.system('clear')

    menu1 = int(input('\nDeseja repetir o programa novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    while menu1 < 1 or menu1 > 2:
        os.system('clear')
        menu1 = int(input('Opção inválida, digite novamente: \n[ 1 ] Sim \n[ 2 ] Não \nR: '))
    if menu1 == 1:
        menu += 1
    elif menu1 == 2:
        print('Fim do programa.')
        break
