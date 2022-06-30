print("\033[1;33m{:#^80}\033[m".format(" Declarando um Triângulo "))
print()
s1 = float(input("\033[35mMedida do primeiro segmento: \033[m"))
s2 = float(input("\033[35mMedida do segundo segmento: \033[m"))
s3 = float(input("\033[35mMedida do terceiro segmento: \033[m"))
print()
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == (s2 + s3) / 2 and s2 == (s1 + s3) / 2 and s3 == (s1 + s2) / 2:
        tr = str("Equilátero")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        tr = str("Isóceles")
    else:
        tr = str("Escaleno")
    print("Os Valores respectivos podem formar um \033[32mtriângulo {}\033[m.".format(tr))
else:
    print("\033[1;31m* Os tais valores não formam um triângulo. *\033[m")