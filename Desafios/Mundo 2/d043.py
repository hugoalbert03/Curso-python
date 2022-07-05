from math import pow
from time import sleep
print("{:#^60}".format("\033[1;33m CALCULO DE IMC \033[m"))
altura = float(input("\033[32mDigite sua altura: \033[m"))
peso = float(input("\033[32mDigite seu peso: \033[m"))
if peso > 300 or peso < 20 or altura > 2.15 or altura < 0.80:
    print("\033[1;31mVALOR INVÁLIDO:\033[m \033[31mCertifique os valores e tente novamente!\033[m")
else:
    imc = peso / pow(altura,int(2))
    print("\033[35mCarregando...\033[m")
    sleep(3)
    if imc < 18.5:
        resIMC = "\033[33mAbaixo do Peso\033[m"
    elif imc < 25:
        resIMC = "\033[32mPeso Ideal\033[m"
    elif imc < 30:
        resIMC = "\033[33mSobre Peso\033[m"
    elif imc < 40:
        resIMC = "\033[31mObesidade\033[m"
    else:
        resIMC = "\033[30;41m Obesidade Mórbida \033[m"
    print()
    print("Seu IMC é de \033[36m{:.1f}\033[m".format(imc))
    print("\033[1;35mSituação:\033[m {}".format(resIMC))