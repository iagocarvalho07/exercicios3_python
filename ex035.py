print('-=-'*20)
print('analisador de triangulos')
print('-=-'*20)
t1 = int(input('primeiro seguimento '))
t2 = int(input('segundo seguimento '))
t3 = int(input('terceiro seguimento '))
if t1 < t2 + t3 and t2 <t1 + t3 and t3 < t1 + t2:
    print('os seguimentos acima podem formar um triagulo')
else:
    print('os seguimentos acima não podem formar um triagulo')
