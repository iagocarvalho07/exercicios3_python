num = int(input('digite um numero inteiro: '))
print('''escolha uma das bases para versão:
[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''' )
opção = int(input('sua opção: '))
if opção == 1:
    print('{} convertido para binario e igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para octal e igual a {}'.format(num, oct(num)))
elif opção ==3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('opção invalida!!! tente novamente')

