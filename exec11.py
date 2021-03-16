# 11. As Organizações Tabajara resolveram dar um aumento de salário
# aos seus colaboradores e lhe contraram para desenvolver o programa
# que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste
# segundo o seguinte critério, baseado no # salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento serrealizado,
# informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Digite o seu salário: '))

if salario <= 280.00:
    print(f'O seu salário antes do reajuste era de R${salario}')
    print('Foi aplicado um aumento de 20% ao seu salário.')
    aumento20 = salario + salario * (20 / 100)
    print(f'Seu novo salário será de R${aumento20}')
elif salario > 280.00 and salario <= 700.00:
    print(f'O seu salário antes do reajuste era de R${salario}')
    print('Foi aplicado um aumento de 15% ao seu salário.')
    aumento15 = salario + salario * (15 / 100)
    print(f'Seu novo salário será de {aumento15}')
elif salario >= 700 and salario <= 1500.00:
    print(f'O seu salário antes do reajuste era de R${salario}')
    print('Foi aplicado um aumento de 10% ao seu salário.')
    aumento10 = salario + salario * (10 / 100)
    print(f'Seu novo salário será de {aumento10}')
elif salario > 1500.00:
    print(f'O seu salário antes do reajuste era de R${salario}')
    print('Foi aplicado um aumento de 5% ao seu salário.')
    aumento5 = salario + salario * (5 / 100)
    print(f'Seu novo salário será de {aumento5}')
