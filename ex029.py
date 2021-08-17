carro = int(input('qual a velociade de um carro '))
if carro >= 80:
    print('voce ultrapassou o limite de velocidade ')
    multa = (carro-80)*7
    print('voce foi multado em R${}'.format(multa))
else:
    print('voçe e uma motorista responsavel, parabens')
print('dirija com segurança')