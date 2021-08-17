n1 = float(input('DIGITE A PRIMEIRA NOTA '))
n2 = float(input('DIGITE A SEGUNDA NOTA '))
MEDIA = (n1 + n2)/2
if MEDIA >= 7:
    print('aprovado')
elif MEDIA >= 5 and MEDIA < 7:
    print('recuperação')
elif MEDIA < 5 :
    print('\033[0:31:44m reprovado \033[0:31:44m ')