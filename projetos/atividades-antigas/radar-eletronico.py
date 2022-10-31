from random import randint
from time import sleep

print('\033[1;30;47mSeu carro passou por um radar eletrônico de 80 km/h')
sleep(5)
speed = randint(0, 160)
if speed <= 80:
    print('Parabéns por manter a velocidade orientada de {}km/h, boa tarde!'.format(speed))
else:
    print('Que pena! Devido a velocidade de {}km/h você foi multado, tome cuidado!'.format(speed))