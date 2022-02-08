from time import sleep
print()
print("{:|^70}".format(" Aumento Salarial "))
print()
vsal = float(input("Digite o valor de seu salario: R$"))
print("Processando...")
sleep(2)
print()
if vsal == 0:
    print("Erro: Valor inválido!")
else:
    if vsal > 1250:
        perc = vsal / 100 * 10
        pc = 10
    else:
        perc = vsal / 100 * 15
        pc = 15
    print("Com {}% de aumento, seu novo salario atualmente será R${:.2f}".format(pc,(vsal + perc)))