from math import sin, cos, tan, radians
ang = float(input("Digite um valor de Ângulo em gráus: "))
sn = sin(radians(ang))
cs = cos(radians(ang))
tg = tan(radians(ang))
print("Analizando o ângulo de {}⁰\nO seno é {:.2f}, \nO cosseno é {:.2f} \nA tangente é {:.2f}".format(ang,sn,cs,tg))