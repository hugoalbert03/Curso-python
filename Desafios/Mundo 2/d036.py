from time import sleep
print("{:*^70}".format(" \033[1;34;42m Emprestimo Salarial Pra Compra de Casa \033[m "));
print()
valIm = float(input("\033[35m* Qual o valor do imóvel?\033[m \033[33mR$")); print("\033[m");
valSal = float(input("\033[35m* Qual é o seu salário?\033[m \033[33m R$")); print("\033[m");
temp = int(input("\033[35m* Quão que tempo você estará disposto à pagar pelo imóvel?\033[m \033[33m(anos) ")); print("\033[m");
print("\033[33mColetando Dados...")
sleep(2)
print("Calculando os resultados...")
porc = 30/100
vPorc = porc * valSal
parceIm = valIm / temp
sleep(5)
print("Analisando sua condição...\033[m")
sleep(3)
print()
if parceIm > vPorc :
    print("\033[1;31mEmpréstimo Negado!\033[m")
    print("Sua parcela é de R${:.2f}".format(parceIm))
    print("Porém 30% de seu salário é R${:.2f}".format(vPorc))
else:
    print("\033[1;32mEMPRÉSTIMO ACEITO COM SUCESSO!\033[m")
    print("Boa Sorte!")