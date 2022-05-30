print("{:|^70}".format("\033[1;36;42mEmprestimo Salarial Pra Compra de Casa\033[m"));
valIm = float(input("Qual o valor do imóvel? R$"));
valSal = float(input("Qual é o seu salário? R$"));
temp = int(input("Quão que tempo você estará disposto à pagar pelo imóvel?(anos) ")) ;
if temp < 10 and temp > 60 or valSal < 500 or valIm < 20000:
    print("Valor não aceito!")
else:
    valPorc = 30/100
    percF = valPorc * valSal
    prestMens = valIm / temp
    print(prestMens)