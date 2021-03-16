# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')

if letra in 'Aa, Ee, Ii, Oo, Uu':
    print(f'{letra}-> é uma vogal')
else:
    print(f'{letra}-> é uma consoante')
