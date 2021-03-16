# 16. Faça um programa que calcule as raízes de uma equação do
# segundo grau, na forma ax2 + bx + c. O programa deverá pedir
# os valores de a, b e c e fazer as consistências, informando ao
# usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não
# é do segundo grau e o programa não deve fazer # pedir os demais
# valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais.
# Informe ao usuário e encerre o # programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz
# real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao
# usuário;

import math

print("digite os termos da equacao a, b e c da equacao ax^2 + bx + c")
a = int(input("digite o termo a ---> "))
if a == 0:
    print("nao é uma equação de segundo grau")
else:
    b = int(input("digite o termo b  ---> "))
    c = int(input("digite o termo c ---> "))
    delta = (math.pow(b, 2) - (4*a*c))
    if delta < 0:
        print(f'delta = {delta} a equacao nao possui raizes reais')
    if delta == 0:
        print(f'delta = {delta} a equacao possui uma raiz')
        raiz = ((-1)*b + math.sqrt(delta))/(2*a)
        print(f'raiz da equacao = {raiz}')
    if delta > 0:
        print(f'delta = {delta} a equacao possui duas raizes')
        raiz1 = ((-1)*b + math.sqrt(delta))/(2*a)
        raiz2 = ((-1)*b - math.sqrt(delta))/(2*a)
        print(f'raiz1 da equacao = {raiz1}')
        print(f'raiz2 da equacao = {raiz2}')
