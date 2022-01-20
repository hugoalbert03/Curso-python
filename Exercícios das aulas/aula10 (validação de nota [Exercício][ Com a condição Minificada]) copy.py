n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print("A sua média foi {:.2f} pontos.".format(m))

print("Você passou de ano!" if m >= 5 else "Você foi reprovado!")