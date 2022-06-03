from time import sleep
print("{:\^70}".format("\033[1;36;42mEmprestimo Salarial Pra Compra de Casa\033[m"));
valIm = float(input("\033[Qual o valor do imóvel? R$"));
valSal = float(input("Qual é o seu salário? R$"));
temp = int(input("Quão que tempo você estará disposto à pagar pelo imóvel?(anos) ")) ;
print("Coletando Dados...")
sleep(2)
print("Calculando os resultados...")
porc = 30/100
vPorc = porc * valSal
parceIm = valIm / temp
sleep(5)
print("Analisando sua condição...")
sleep(3)
if parceIm > vPorc :
    print("Empréstimo Negado!")
    print("Sua parcela é de R${:.2f}".format(parceIm))
    print("Porém 30% de seu salário é R${:.2f}".format(vPorc))
else:
    print("EMPRÉSTIMO ACEITO COM SUCESSO!")
    print("Boa Sorte!")