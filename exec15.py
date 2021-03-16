# 15. Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
# isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dos lados
# for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
print('Formação de um triângulo.')

l1 = float(input('Digite o 1º lado: '))
l2 = float(input('Digite o 2º lado: '))
l3 = float(input('Digite o 3º lado: '))

if l1 + l2 > l3:
    if l1 == l2 and l1 == l3:
        print('Triângulo Equilátero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Triângulo Isósceles')
    elif l1 != l2 and l3 or l2 != l1 and l3 or l1 != l3:
        print('Triângulo Escaleno')

else:
    print('É impossivel ser um triângulo')
