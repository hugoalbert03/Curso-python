import time
print("{:*^50}".format("Radar"))
velUsr = float(input("Digite a velocidade do veículo em KM/h: "))
print("Processando as informções...")
time.sleep(4)
print("")
if velUsr > 80:
    vUlt = velUsr - 80
    Sans = vUlt * 7.00
    print("Você foi multado por andar {:.1f} KM/h acima do permitido! \nSua multa será equivalente à R$ {:.2f}".format(vUlt,Sans))
else:
    print("Veículo na velocidade permitida!")
print("Tenha um bom dia! Dirija de forma segura!")    