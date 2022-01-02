sal = float(input("Digite o valor de seu salário: R$"));
per = sal/100 * 15;
print("Seu salário de R${:.2f} reajustado em 15% é equivalente à R${:.2f}.".format(sal,(sal+per)));