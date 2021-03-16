# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia
# o número de litros vendidos, o tipo de combustível (codificado da seguinte
# forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo
# cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do
# litro do álcool é R$ 1,90.

combustivel = input("Digite o combustivel-> [A-Alcool] ou [G-Gasolina]: ")
litros = float(input("Quantos litros deseja abastecer?: "))

if combustivel in 'Aa':
    print("O combustivel escolhido foi Alcool = 1.90/L")

    if litros <= 20.00:
        valor1 = litros * 1.90
        desc1 = valor1 * 0.03
        total_a_pagar1 = valor1 - desc1

        print(f'O preco a ser pago é: {total_a_pagar1:.2f}')

    if litros > 20.00:
        valor2 = litros * 1.90
        desc2 = valor2 * 0.05
        total_a_pagar2 = valor2 - desc2

        print(f'O preco a ser pago é: {total_a_pagar2:.2f}')

if combustivel in 'Gg':
    print("O combustivel escolhido foi Gasolina = 2.50/L")

    if litros <= 20.00:
        valor3 = litros * 2.50
        desc3 = valor3 * 0.04
        total_a_pagar3 = valor3 - desc3

        print(f'O preco a ser pago é: {total_a_pagar3:.2f}')

    if litros > 20.00:
        valor4 = litros * 2.50
        desc4 = valor4 * 0.06
        total_a_pagar4 = valor4 - desc4
        print(f'O preco a ser pago é: {total_a_pagar4:.2f}')
