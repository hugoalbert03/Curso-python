nUser = int(input("Digite uma numeração: "))
nRes = nUser % 2
if nRes == 1:
    print("O {} é um número ímpar!".format(nUser))
else:
    print("O {} é um número par!".format(nUser))