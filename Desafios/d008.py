mval = float(input('Distância em metros(M): '));
print("")
print("{:=^50}".format(("RESULTADO")))
print("")
print("{:.1f}km \n{:.1f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm.".format(float(mval/1000),float(mval/100),(float(mval/10)),(float(mval*10)),(float(mval*100)),(float(mval*1000))));
print("")