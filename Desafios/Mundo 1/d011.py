print("")
print("{:*^70}".format("Analize de Pintura de Parede"));
print("")
larg = float(input("Digite a largura da parede(M): "))
alt = float(input("Digite a altura da parede(M): "));
tint = float(2)
print("")
print("{:=^70}".format(("Resultado")))
print("")
print("Sua parede tem a dimensão de {:.1f}x{:.1f} equivalente à {:.1f}M² \nSerá necessário {:.1f} litros de tinta para sua pintura".format(larg,alt,(larg*alt),(larg*alt/tint)))
print("")