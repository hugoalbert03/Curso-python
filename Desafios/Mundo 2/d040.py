from time import sleep
print("\033[1;33m{:*^60}\033[m".format("Calculo de Notas Escolar"))
nt1 = float(input("\033[32mPrimeira Nota: \033[m"))
nt2 = float(input("\033[32mSegunda Nota: \033[m"))
nfinal = (nt1 + nt2) / 2
if nt1 < 0 or nt2 < 0 or nt1 > 10 or nt2 > 10:
    print("\033[5;31mValor inválido\033[m")
else:
    print("Carregando...")
    sleep(3)
    if nfinal == 1:
        plu = str("ponto")
    elif nfinal > 1:
        plu = str("pontos")
    else:
        plu = str("")
    print("Sua nota foi \033[35m{:.1f}\033[m {}.".format(nfinal,plu))
    if nfinal < 5:
        print("\033[1;31mAluno reprovado!\033[m")
    elif nfinal >= 5 and nfinal < 7:
        print("\033[1;33mAluno em recuperação!\033[m")
    else:
        print("\033[1;32mAluno aprovado!\033[m")