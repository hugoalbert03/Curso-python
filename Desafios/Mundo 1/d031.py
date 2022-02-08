from time import sleep
print("{:-^50}".format("Cobrador de Distância de Viagem"))
dist = float(input("Qual a distância em KM da Viagem? "))
print("Processando...")
sleep(2)
if dist == 0:
    print()
    print("A distância não pode equivaler a 0")
elif dist < 0:
    print()
    print("A distância não pode ser menor que 0")
else:
    print()
    if dist <= 200:
        df = 0.50 * dist
    else:
        df = 0.45 * dist
    print("Você está prestes a fazer uma viagem de {:.1f}Km \nA passagem custará R${:.2f}".format(dist,df))