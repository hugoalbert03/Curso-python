from time import sleep
print("{:*^70}".format(" \033[1;34;42m Emprestimo Salarial Pra Compra de Casa \033[m "));
print()
valIm = float(input("\033[35m* Qual o valor do imóvel?\033[m \033[33mR$")); print("\033[m");
valSal = float(input("\033[35m* Qual é o seu salário?\033[m \033[33m R$")); print("\033[m");
temp = int(input("\033[35m* Quão que tempo você estará disposto à pagar pelo imóvel?\033[m \033[33m(anos) ")); print("\033[m");
print("\033[36m Coletando Dados...")
sleep(2)
print(" Calculando os resultados...")
porc = 30/100
vPorc = porc * valSal
parceIm = valIm / (temp * 12)
sleep(5)
print(" Analisando sua condição...\033[m")
sleep(3)
print()
if parceIm > vPorc :
    print("\033[1;31mEmpréstimo Negado!\033[m")
    print("- As parcelas do imóvel divididas em {} anos é de \033[1;32mR${:.2f} mensal\033[m".format(temp,parceIm))
    print("- Por conseguite 30% de seu salário é de \033[1;31mR${:.2f}\033[m".format(vPorc))
else:
    print("\033[1;32mEMPRÉSTIMO ACEITO COM SUCESSO!\033[m")
    print("- Seu salário e o tempo que você desejou pagar atenderam as expectativas de empréstimo!")
    print("- Boa Sorte!")
