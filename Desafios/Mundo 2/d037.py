print("{:=^90}".format("Base de Conversão"))
print()
num = int(input("Digite um valor: "))
print("""

Escolha as opções de bases numéricas

[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadeximal

""")

op = int(input("Opção: "))
print()
if op < 1 or op > 3 :
    print("Opção inválida")
else:
    if op == 1:
        print("{} convertido em BINÁRIO é igual a {}".format(num,bin(num)[2:]))
    elif op == 2:
        print("{} convertido em OCTAL é igual a {}".format(num,oct(num)[2:]))
    else:
        print("{} convertido em HEXADECIMAL é igual a {}".format(num,hex(num)[2:]))
