import random

cont = 0
cont1 = 1
pt_1 = []
pt_2 = []
pt_3 = []
pt_4 = []
gp_a = []
gp_b = []
gp_c = []
gp_d = []

total = int(input('Digite o tamanho do grupo(ex: 4): '))
if total != 4:
    total = 4
    print('Número inválido! A versão atual só permite 4 equipes.')

for clubes in range(0, total):
    print('\n{}° GRUPO'.format(cont1))
    print('--=--' * 10)
    pote1 = str(input('Digite o nome do {}° clube do Pote 1: '.format(cont1)))
    pt_1.append(pote1)
    pote2 = str(input('Digite o nome do {}° clube do Pote 2: '.format(cont1)))
    pt_2.append(pote2)
    pote3 = str(input('Digite o nome do {}° clube do Pote 3: '.format(cont1)))
    pt_3.append(pote3)
    pote4 = str(input('Digite o nome do {}° clube do Pote 4: '.format(cont1)))
    pt_4.append(pote4)
    cont1 += 1

for clubes1 in range(1, total):
    if cont == 0:
        pote1 = random.choice(pt_1)
        gp_a.append(pote1)
        pt_1.remove(pote1)
        pote2 = random.choice(pt_1)
        gp_b.append(pote2)
        pt_1.remove(pote2)
        pote3 = random.choice(pt_1)
        gp_c.append(pote3)
        pt_1.remove(pote3)
        pote4 = random.choice(pt_1)
        gp_d.append(pote4)
        pt_1.remove(pote4)
    if cont == 1:
        pote1 = random.choice(pt_2)
        gp_a.append(pote1)
        pt_2.remove(pote1)
        pote2 = random.choice(pt_2)
        gp_b.append(pote2)
        pt_2.remove(pote2)
        pote3 = random.choice(pt_2)
        gp_c.append(pote3)
        pt_2.remove(pote3)
        pote4 = random.choice(pt_2)
        gp_d.append(pote4)
        pt_2.remove(pote4)
    if cont == 2:
        pote1 = random.choice(pt_3)
        gp_a.append(pote1)
        pt_3.remove(pote1)
        pote2 = random.choice(pt_3)
        gp_b.append(pote2)
        pt_3.remove(pote2)
        pote3 = random.choice(pt_3)
        gp_c.append(pote3)
        pt_3.remove(pote3)
        pote4 = random.choice(pt_3)
        gp_d.append(pote4)
        pt_3.remove(pote4)
    if cont == 3:
        pote1 = random.choice(pt_4)
        gp_a.append(pote1)
        pt_4.remove(pote1)
        pote2 = random.choice(pt_4)
        gp_b.append(pote2)
        pt_4.remove(pote2)
        pote3 = random.choice(pt_4)
        gp_c.append(pote3)
        pt_4.remove(pote3)
        pote4 = random.choice(pt_4)
        gp_d.append(pote4)
        pt_4.remove(pote4)
    cont += 1
print('\nGrupo A\n{}\nGrupo B\n{}\nGrupo C\n{}\nGrupo D\n{}'.format(gp_a, gp_b, gp_c, gp_d))
