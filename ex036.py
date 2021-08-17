casa = int(input('digite o valor da casa R$'))
s = int(input('salario do comprador '))
f = int(input('quantos anos de financiamento ? '))
prestação = casa / (f*12)
minimo = s * 30/100
print('para pagar a casa de {} em {} anos, a prestação será de R${}'.format(casa, f, prestação))
if prestação <=minimo:
    print('emprestimo concedido')
else:
    print('emprestimo negado')