salario = float(input('qual o salario do funcionario? '))
if salario >= 1250:
    s = (salario*115/100)
else:
    s =(salario*110/100)
print('quem ganhava {} passa a ganhar {} agora'.format(salario, s))