from time import sleep
# Atribuição de Variáveis
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
print("Calculando...")
sleep(4)
print()
#Organização em vetorização
numb = [n1,n2,n3]
print("Dos números do vetor: {}".format(numb))
#Condicionamento para o número maior
if n1 > n2 and n1 > n3:
    resMr = n1
elif n2 > n1 and n2 > n3:
    resMr = n2
else:
    resMr = n3
print("O maior número foi {}".format(resMr))
#Condicionamento para o número menor
if n1 < n2 and n1 < n3:
    resMn = n1
elif n2 < n1 and n2 < n3:
    resMn = n2
else:
    resMn = n3
print("E o menor número foi {}".format(resMn))