seg1 = float(input("Medida do primeiro segmento: "))
seg2 = float(input("Medida do segundo segmmento: "))
seg3 = float(input("Medida do terceiro segmento: "))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("Os três segmentos formam um triângulo")
else:
    print("Os três segmentos NÃO formam um triângulo")