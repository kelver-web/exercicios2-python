# 6. Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
num3 = float(input('Digite o 3º número: '))

if num1 > num2 and num1 > num3:
    print(f'O maior número é -> {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior número é -> {num2}')
elif num3 > num1 and num3 > num2:
    print(f'O maior número é -> {num3}')
elif num1 == num2 == num3:
    print(f'Os números {num1}, {num2} e {num3} são iguais')
