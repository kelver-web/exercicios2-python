# 3. Faça um Programa que verifique se uma letra digitada é
# "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.

sexo = input('Digite o seu sexo:  ')

if sexo in 'Mm':
    print(f'Masculino {sexo}')
elif sexo in 'Ff':
    print(f'Feminino {sexo}')
else:
    print('Letra não faz parte da identidade')
