from datetime import date
print("\033[1;34m{:#^70}\033[m".format(" Confederação Nacional de Natação - CNN "))
print()
dAtual = date.today().year
dNasc = int(input("\033[33mDigite o seu ano de nascimento: \033[m"))
idade = dAtual - dNasc
if idade < 1 or idade > 90:
    print()
    print("\033[1;31mIDADE INVÁLIDA!\033[m")
else:
    if idade <= 9:
        cat = str("Mirim")
    elif idade > 9 and idade <= 14:
        cat = str("Infantil")
    elif idade > 14 and idade <= 19:
        cat = str("Junior")
    elif idade > 19 and idade <= 25:
        cat = str("Sênior")
    else:
        cat = str("Master")
    print()
    print("Com a idade de \033[1;36m{} anos\033[m você faz parte da categoria \033[1;36m{}\033[m.".format(idade,cat))