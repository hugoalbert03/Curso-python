from datetime import date
ano = int(input("Digite o ano, Caso queira a tata a data atual digite 0: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é um ano Bisexto!".format(ano))
else:
    print("O ano de {} não é Bisexto!".format(ano))

# 1 - Tem que ser feito a divisão modular por quatro!
# 2 - O número em que a divisão modular for zero é o número do ano bisexto!
#   1 de 2 - Números divisiveis modularmente por 100 não pode ser igual a zero, pois a divisão dará 0 a cada século com final 0!
#   2 de 2 - Números divisiveis por 400 tem que ser igual a 0, ou seja, de quatro em quatro séculos é bisexto!