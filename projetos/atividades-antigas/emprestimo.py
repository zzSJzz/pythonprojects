import math
from time import sleep

valor = float(input('Digite o VALOR DA CASA: '))
salario = float(input('Digite seu SALÁRIO MENSAL: '))
anos = int(input('Em quantos anos você irá pagar o financiamento: '))
sleep(5)
max_emp = salario * 0.3
val_mensal = valor / (anos * 12)
if val_mensal <= max_emp:
    print('Parabéns!! Seu empréstimo de R${:.2f} foi aceito. Você pagará R${:.2f} por mês.'.format(valor, val_mensal))
else:
    print('Seu empréstimo foi negado pois o empréstimo de R${:.2f} supera os 30% do seu salário mensal de R${:.2f}'.format(val_mensal, max_emp))

