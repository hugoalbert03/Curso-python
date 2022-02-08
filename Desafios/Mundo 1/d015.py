print("");
print("{:=^50}".format(("Aluguel de Carro")));
print("")
d = int(input("Digite a quantidade de dias alugado: "));
dist = float(input("Digite a quantidade de KM percorrido: "));
td = d * 60;
tds = dist * 0.15;
totp = float(td+tds);
print("")
print("*** O total a pagar pelo carro é de R${:.2f} ***".format(totp));