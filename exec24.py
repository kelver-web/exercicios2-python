# 24. Faça um Programa que leia 2 números e em seguida pergunte
# ao usuário qual operação ele deseja realizar. O resultado da
# operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.


n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro: '))
print('''Qual operação deseja fazer?
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir''')
opcao = input('Escolha um opção: ')

if opcao == '1':
    soma = n1 + n2
    print(f'{int(n1)} + {int(n2)} = {int(soma)}')
    if soma % 2 == 0:
        print(f'{int(soma)} é par')
    else:
        print(f'{int(soma)} é ímpar')

    if soma > 0:
        print(f'{int(soma)} é positivo')
    else:
        print(f'{soma} é negativo')

    if soma // 1 == soma:
        print(f'{int(soma)} é um inteiro')
    else:
        print(f'{soma} é decimal')


if opcao == '2':
    sub = n1 - n2
    print(f'{int(n1)} - {int(n2)} = {int(sub)}')
    if sub % 2 == 0:
        print(f'{int(sub)} é par')
    else:
        print(f'{int(sub)} é ímpar')

    if sub > 0:
        print(f'{int(sub)} é positivo')
    else:
        print(f'{sub} é negativo')

    if sub // 1 == sub:
        print(f'{int(sub)} é um inteiro')
    else:
        print(f'{sub} é decimal')

if opcao == '3':
    mult = n1 * n2
    print(f'{int(n1)} x {int(n2)} = {int(mult)}')
    if mult % 2 == 0:
        print(f'{int(mult)} é par')
    else:
        print(f'{int(mult)} é ímpar')

    if mult > 0:
        print(f'{int(mult)} é positivo')
    else:
        print(f'{mult} é negativo')

    if mult // 1 == mult:
        print(f'{int(mult)} é um inteiro')
    else:
        print(f'{mult} é decimal')

if opcao == '4':
    dividi = n1 / n2
    print(f'{int(n1)} / {int(n2)} = {int(dividi)}')
    if dividi % 2 == 0:
        print(f'{int(dividi)} é par')
    else:
        print(f'{int(dividi)} é ímpar')

    if dividi > 0:
        print(f'{int(dividi)} é positivo')
    else:
        print(f'{dividi} é negativo')

    if dividi // 1 == dividi:
        print(f'{int(dividi)} é um inteiro')
    else:
        print(f'{dividi} é decimal')
