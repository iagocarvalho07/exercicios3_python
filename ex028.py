from random import randint
computador = randint(0, 5)
print( '-=-' * 20)
print('vou pensar em um numero de 0 a 5, tente adivinhar....')
print( '-=-' * 20)
jogador = int(input('em que numero em pensei? '))
print('processando...')
if jogador == computador:
    print('parabens! voce conseguiu vencer')
else:
    print('ganhei, vc perdeu, eu pensei em {} '.format(computador))
