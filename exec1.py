# 1. Faça um Programa que peça dois números e imprima o maior deles.
n1 = float(input('Digite um número:  '))
n2 = float(input('Digiete outro:  '))

if n1 > n2:
    print(f'O maior é {n1}')

elif n2 > n1:
    print(f'O maior é {n2}')

else:
    if n1 == n2:
        print(f'Os números {n1} e {n2} são iguais')
