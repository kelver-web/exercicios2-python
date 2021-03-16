# 8. Faça um programa que pergunte o preço de três produtos
# e informe qual produto você deve comprar, sabendo que a decisão
# é sempre pelo mais barato.

prod1 = float(input('Digite o preço do 1º produto:  '))
prod2 = float(input('Digite o preço do 2º produto:  '))
prod3 = float(input('Digite o preço do 3º produto:  '))

print('Sabendo que a decisão de compra é pelo produto mais barato.')

if prod1 < prod2 and prod1 < prod3:
    print(f'Você deve comprar o produto no valor de R${prod1:.2f}')
elif prod2 < prod1 and prod2 < prod3:
    print(f'Você deve comprar o produto no valor de R${prod2:.2f}')
elif prod3 < prod1 and prod3 < prod2:
    print(f'Você deve comprar o produto no valor de R${prod3:.2f}')
