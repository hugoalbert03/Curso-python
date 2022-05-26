#Treino 01
#nome = str(input("\033[32m Qual é o seu nome? \033[m \033[33m")); print("\033[m")
#if nome == "Hugo" or nome == "hugo":
#    print("\033[32m Que belo nome!\033[m")
#    dia = "bom"
#else:
#    print("\033[33m Vai se lascar!\033[m")
#    dia = "mau"
#print('\033[35mTenha um {} dia, {}\033[m'.format(dia,nome))

#treino 02
nome = str(input("\033[32m Qual é o seu nome? \033[m \033[33m")); print("\033[m")
if nome == "Hugo" or nome == "hugo":
    print("\033[32m Que belo nome!\033[m")

elif nome in "Paulo Pedro João Carlos Rodrigo":
    print("Seu nome é bem comum!")
else:
    print("Seu nome é bem normal!")