# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista = []

for i in range(1, 4):
    num = int(input(f'Digite o {i}º número: '))
    lista.append(num)

lista.sort(reverse=True)
print(lista)
