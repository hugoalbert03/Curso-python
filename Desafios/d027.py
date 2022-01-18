nome = str(input("Digite seu nome completo: ")).strip().split()
print("Muito prazer te conhacer!")
print("Primeiro nome = {}".format(nome[0]))
vnome = int(len(nome)) - 1
print("Último nome = {}".format(nome[vnome]))