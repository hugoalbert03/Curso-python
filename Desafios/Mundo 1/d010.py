print("{:=^50}".format(("Conversor de Moedas")));
monrs = float(input("Quanto em dinheiro você possui na carteira? R$"));
mondol = float(3.27);
moneur = float(0.16);
monps = float(18.02)
print("");
print("Com R${:.2f} você pode comprar: \nUS${:.2f} \nЄ{:.2f} \n${:.2f}".format(monrs,(monrs/mondol), (monrs*moneur), (monrs*monps)));