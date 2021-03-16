# 14. Faça um programa que lê as duas notas parciais obtidas
# por um aluno numa disciplina ao longo de um semestre, e
# calcule a sua média. A atribuição de conceitos obedece à
# tabela abaixo:
# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0     A
# Entre 7.5 e 9.0      B
# Entre 6.0 e 7.5      C
# Entre 4.0 e 6.0      D
# Entre 4.0 e zero     E
# O algoritmo deve mostrar na tela as notas, a média,
# o conceito correspondente e a mensagem “APROVADO” se
# o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


print('''Média de Aproveitamento  Conceito
Entre 9.0 e 10.0     A
Entre 7.5 e 9.0      B
Entre 6.0 e 7.5      C
Entre 4.0 e 6.0      D
Entre 4.0 e zero     E''')

n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
media = (n1 + n2) / 2

print(f'Suas notas foram - {n1} e {n2}')
print(f'Sua média foi - {media}')

if media <= 10 and media >= 9:
    notaA = media
    print(f'Nota {notaA} - A')
elif media >= 7.5 and media <= 9:
    notaB = media
    print(f'Nota {notaB} - B')
elif media >= 6 and media <= 7.5:
    notaC = media
    print(f'Nota {notaC} - C')
elif media <= 6 and media >= 4:
    notaD = media
    print(f'Nota {notaD} - D')
elif media <= 4:
    notaE = media
    print(f'Nota {notaE} - E')
