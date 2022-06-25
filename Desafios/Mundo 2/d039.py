from time import sleep
from datetime import date
print("{:#^70}".format(" \033[1;32mValidação de Idade para o Exército\033[m "))
print()
a = date.today().year
DtNasc = int(input("\033[33mAno de nascimento\033[m> "))
id = a - DtNasc
print()
if DtNasc < 1930 or DtNasc > (a - int(8)):
    print("\033[31mData ou idade Inválida!\033[m")
else:
    print("\033[35mValidando...\033[m")
    sleep(4)
    print()
    if id < 17:
        print("\033[1;33mVocê ainda irá se alistar!\033[m")
        print("\033[36m- Faltam {} anos para o seu alistamento!\033[m".format((int(18) - id)))
        print("\033[36m- Seu alistamento será em {} \033[m".format((DtNasc + int(18))))
    elif id == 18:
        print("\033[1;32mÉ hora de você se alistar IMEDIATAMENTE!\033[m")
        print("\033[36m- Vá até uma junta militar próximo a sua residência e aliste-se \033[m")
    else:
        print("\033[1;31mJá passou o seu tempo de alistamento!\033[m")
        print("\033[36m- Quem nasceu em {} tem {} anos em {}".format(DtNasc,id,a))
        idPr = int(18) - id
        idPrForm = idPr - (idPr * 2)
        if idPrForm == 1:
            ano = "ano"
        else:
            ano = "anos"
        print("- Já se passaram {} {} após seu prazo de alistamento.".format(idPrForm,ano))
        print("- Seu alistamento foi no ano de {}\033[m".format((DtNasc + int(18))))
print()