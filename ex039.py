from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento '))
idade = atual - nasc
print('quem nasceu em {} Tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('voce tem que se alistar imediatamente')
elif idade < 18:
    saldo = idade - 18
    ano = atual + saldo
    print('voce ainda n tem 18 anos, ainda falta {} anos para o alistamento'.format(saldo))
    print('seu alistamento sera em {} '.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('voce tem mais de 18 anos, devaria ter se alistado ha {} anos'.format(saldo))
    print('seu alistamento seria em {} '.format(ano))