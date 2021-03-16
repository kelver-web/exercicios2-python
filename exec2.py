# 2. Faça um Programa que peça um valor e mostre na tela
# se o valor é positivo ou negativo.

valor = float(input('Digite um valor:  '))

if valor >= 0:
    print(f'Esse valor {valor} é possitivo')
else:
    if valor < 0:
        print(f'Esse valor {valor} é negativo')
