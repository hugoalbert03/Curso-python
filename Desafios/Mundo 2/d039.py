from time import sleep
print("{:#^70}".format(" \033[1;32mValidação de Idade para o Exército\033[m "))
print()
DtNasc = int(input("\033[33mAno de nascimento\033[m> "))
id = int(2022) - DtNasc
print()
if DtNasc < 1930 or DtNasc > 2014:
    print("Data Inválida")
else:
    print("\033[35mValidando...\033[m")
    sleep(4)
    print()
    if id < 17:
        print("\033[1;33mVocê ainda irá se alistar!\033[m")
        print("\033[36mFaltam {} anos para o seu alismtento!\033[m".format((int(18) - id)))
    elif id == 18:
        print("\033[1;32mÉ hora de você se alistar!\033[m")
    else:
        print("\033[1;31mJá passou o seu tempo de alistamento!\033[m")
        print("\033[36m- Quem nasceu em {} tem {} anos em {}".format(DtNasc,id,(int(2022))))
        idPr = int(18) - id
        idPrForm = idPr - (idPr * 2)
        if idPrForm == 1:
            ano = "ano"
        else:
            ano = "anos"
        print("- Já se passaram {} {} após seu prazo de alistamento.".format(idPrForm,ano))
        print("- Seu alistamento foi no ano de {}\033[m".format((DtNasc + int(18))))
print()