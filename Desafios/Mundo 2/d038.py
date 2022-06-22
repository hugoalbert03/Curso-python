print("\033[33m{:=^40}\033[m".format("Comparação de Números"))
print()
n1  = int(input("\033[36mDigite o primero numero: \033[m"))
n2 = int(input("\033[36mDigite o segundo numero: \033[m"))
if n1 == n2:
    print("\033[31mNão existe valor maior, os dois são iguais. \033[m")
else:
    if n1 > n2:
        result = "\033[32mPRIMEIRO\033[m"
    else:
        result = "\033[33mSEGUNDO\033[m"
    print("O {} número é o maior".format(result))
print()