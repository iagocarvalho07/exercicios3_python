viagem = int(input('qual a distancia da sua viajem?..'))
print('voce esta prestes a começar uma viagem de {}km'.format(viagem))
if viagem >= 200:
    print('o preço de sua passagem será {}'.format(viagem*0.50))
else:
    print('o preço de sua passagem será {}'.format(viagem*0.45))
print('boa viagem ')