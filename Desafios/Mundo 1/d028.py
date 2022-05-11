from random import randint #Importação de um elemento único do Random
from time import sleep
print("-=-" * 30)
print("Pensarei em um número de 1 a 10, tente adivinhar...")
print("-=-" * 30)
npc = randint(1,10) #O computador sorteia um número
nusr = int(input("Pense em um numero? ")) #O usuário pensa em um número
print("Processando...")
if nusr > 10 or nusr < 1: #O computador avalia se o usuário estrapolou o limite da resposta
    print("Numeração excedida! A regra é digitar uma numeração entre 1 a 10")
else:
    sleep(3)
    if nusr == npc: #O computador avalia se o usuário venceu ou perdeu
        print("Parabéns, você conseguiu me vencer!")
    else:
        print("Você perdeu!\nPensei em {} mas você digitou {}.".format(npc, nusr))
        print("Tente na proxima!")