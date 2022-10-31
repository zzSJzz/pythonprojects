import random
sorteio = []
A = []
B = []
C = []
D = []
cont = 1
cont1 = 1
for z in range(0, 16):
    x = str(input('Digite o nome do {}° país: '.format(cont)))
    sorteio.append(x)
    cont += 1
for z1 in range(0, 16):
    test = random.choice(sorteio)
    if cont1 <= 4:
        A.append(test)
        sorteio.remove(test)
    elif cont1 <= 8:
        B.append(test)
        sorteio.remove(test)
    elif cont1 <= 12:
        C.append(test)
        sorteio.remove(test)
    elif cont1 <= 16:
        D.append(test)
        sorteio.remove(test)
    cont1 += 1
print('Grupo A \n {} \n Grupo B \n {} \n Grupo C \n {} \n Grupo D \n {}'.format(A, B, C, D))