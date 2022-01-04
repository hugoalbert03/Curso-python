#from math import pow, sqrt
#c1 = float(input("Digite o valor do cateto oposto: "))
#c2 = float(input("Digite o valor do cateto adjascente: "))
#hip = pow(c1,2) + pow(c2,2)
#print("A hipotenusa mede {:.2f}cm".format(sqrt(hip)))

from math import hypot

catO = float(input('Informe o valor do cateto oposto: '))
catA = float(input('Informe o valor do cateto adjascente: '))
print('A hipotenusa é {:.2f}'.format(hypot(catO,catA)))
