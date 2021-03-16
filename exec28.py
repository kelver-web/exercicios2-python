# 28. O Hipermercado Tabajara está com uma promoção de carnes
# que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas
# um dos tipos de carne da promoção, porém não há limites para a quantidade
# de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa
# que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom
# fiscal, contendo as informações da compra: tipo e quantidade de carne, preço
# total, tipo de pagamento, valor do desconto e valor a pagar.

print('=== Promoção das Carnes do Supermercado Tabajara ===')
print('''               Escolha uma opção
===============================================================
|                        Até 5kg               Acima de 5kg    |
|[A]-----> Alcatra       R$ 5.90 por kg        R$ 6.80 por kg  |
|[P]-----> Picanha       R$ 6.90 por kg        R$ 7.80 por kg  |
===============================================================''')
opcao = input('Escolha uma opção---> ')
quantidade = float(input('Digite a quantidade---> '))
print('''=== Aceitamos ===
-----> Dinheiro
-----> Cartão''')
tipo_pag = input('Digite o tipo de pagamento---> ')

if opcao in 'Aa' and tipo_pag in 'dinheiro'.lower():
    if quantidade <= 5:
        total1 = quantidade * 5.90
        print('========== Cupom Fiscal ==========')
        print('-------Informações da compra------')
        print('Tipo da carne -----------------> Alcatra')
        print(f'Quantidade -------------------> {quantidade}Kg')
        print(f'tipo de pagamento ------------> {tipo_pag} ')
        print(f'Valor a pagar ----------------> R${total1:.2f}')

    else:
        total2 = quantidade * 6.80
        print('========== Cupom Fiscal ==========')
        print('-------Informações da compra------')
        print('Tipo da carne -----------------> Alcatra')
        print(f'Quantidade -------------------> {quantidade}Kg')
        print(f'tipo de pagamento ------------> {tipo_pag}')
        print(f'Preço Total ------------------> {total2:.2f}')

if opcao in 'Aa' and tipo_pag in 'cartao'.lower():
    if quantidade <= 5:
        total3 = quantidade * 5.90
        desconto1 = total3 - (total3 * 0.05)
        print('========== Cupom Fiscal ==========')
        print('-------Informações da compra------')
        print('Tipo da carne -----------------> Alcatra')
        print(f'Quantidade -------------------> {quantidade}Kg')
        print(f'Valor a pagar ----------------> R${total3:.2f}')
        print(f'tipo de pagamento ------------> {tipo_pag} ')
        print(f'Total de desconto ------------> R${total3 * 0.05:.2f}')
        print(f'Valor Total com desconto -----> R${desconto1:.2f}')

    else:
        total4 = quantidade * 6.80
        desconto2 = total4 - (total4 * 0.05)
        print('========== Cupom Fiscal ==========')
        print('-------Informações da compra------')
        print('Tipo da carne -----------------> Alcatra')
        print(f'Quantidade -------------------> {quantidade}Kg')
        print(f'Preço Total ------------------> {total4:.2f}')
        print(f'tipo de pagamento ------------> {tipo_pag}')
        print(f'Total de desconto ------------> R${total4 * 0.05:.2f}')
        print(f'Valor desconto ---------------> R${desconto2:.2f}')


if opcao in 'Pp' and tipo_pag in 'dinheiro'.lower():
    if quantidade <= 5:
        total5 = quantidade * 6.90
        print(f'{total5:.2f}')
        print('========== Cupom Fiscal ==========')
        print('-------Informações da compra------')
        print('Tipo da carne -----------------> Picanha')
        print(f'Quantidade -------------------> {quantidade}Kg')
        print(f'tipo de pagamento ------------> {tipo_pag} ')
        print(f'Valor a pagar ----------------> R${total5:.2f}')

    else:
        total6 = quantidade * 7.80
        print('========== Cupom Fiscal ==========')
        print('-------Informações da compra------')
        print('Tipo da carne -----------------> Picanha')
        print(f'Quantidade -------------------> {quantidade}Kg')
        print(f'tipo de pagamento ------------> {tipo_pag}')
        print(f'Preço Total ------------------> {total6:.2f}')

if opcao in 'Pp' and tipo_pag in 'cartao'.lower():
    if quantidade <= 5:
        total7 = quantidade * 6.90
        desconto3 = total7 - (total7 * 0.05)
        print('========== Cupom Fiscal ==========')
        print('-------Informações da compra------')
        print('Tipo da carne -----------------> Picanha')
        print(f'Quantidade -------------------> {quantidade}Kg')
        print(f'Valor a pagar ----------------> R${total7:.2f}')
        print(f'tipo de pagamento ------------> {tipo_pag} ')
        print(f'Total de desconto ------------> R${total7 * 0.05:.2f}')
        print(f'Valor Total com desconto -----> R${desconto3:.2f}')

    else:
        total8 = quantidade * 7.80
        desconto4 = total8 - (total8 * 0.05)
        print('========== Cupom Fiscal ==========')
        print('-------Informações da compra------')
        print('Tipo da carne -----------------> Picanha')
        print(f'Quantidade -------------------> {quantidade}Kg')
        print(f'Valor a pagar ----------------> R${total8:.2f}')
        print(f'tipo de pagamento ------------> {tipo_pag}')
        print(f'Total de desconto ------------> R${total8 * 0.05:.2f}')
        print(f'Valor Total com desconto ---------------> R${desconto4:.2f}')
