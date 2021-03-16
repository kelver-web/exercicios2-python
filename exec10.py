# 10. Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

print('Em que Turno você estuda.')
print('''
[M] Matutino
[V] Vespertino
[N] Noturno''')
opcao = input('Escolha uma opção:  ')

if opcao in 'Mm':
    print('Bom dia')
elif opcao in 'Vv':
    print('Boa tarde')
elif opcao in 'Nn':
    print('Boa noite')
