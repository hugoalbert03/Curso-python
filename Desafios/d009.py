v = int(input("Digite um numero: "))
num = int(0)
print("")
print('Tabuada de {}'.format(v))
print("")
while num < 10:
    num += 1
    print('{} x {} = {}'.format(v,num,(v*num)))