# 20. Faça um Programa para leitura de três notas parciais
# de um aluno. O programa deve calcular a média alcançada
# por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7,
# com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7,
# com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
n3 = float(input('Digite a 3º nota: '))
media = (n1 + n2 + n3) / 3

if media == 10:
    print(f'Você alcansou a média de {media} - Sua Nota foi ecxelente!!!')
elif media >= 7:
    print(f'Você alcansou a média de {media} - Aprovado')
elif media < 7:
    print(f'Você alcansou a média de {media} - Reprovado')
