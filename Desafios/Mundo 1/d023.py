val = int(input("Digite um numero de 0 à 9999: "))
u = val // 1 % 10
d = val // 10 % 10
c = val // 100 % 10
m = val // 1000 % 10
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))