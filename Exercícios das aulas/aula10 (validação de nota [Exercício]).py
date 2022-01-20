n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("A sua média foi {:.2f} pontos.".format(m))

if m >= 5:
    print("Você foi aprovado! Parabéns!")
else:
    print("Você foi reprovado! Que pena!")
