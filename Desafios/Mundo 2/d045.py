from random import choice
from emoji import emojize
from time import sleep
print("{:=^70}".format(" \033[1;35mJOKEMPÔ - Famso pedra, papel e tesoura\033[m "))
print('''\033[1;33m
Escolha uma das opções:
\033[m\033[1;32m
[1] Pedra
[2] Papel
[3] Tesoura
\033[m
''')
opc = int(input("\033[36mDigite sua opção: \033[m\033[32m"))
print("\033[m")
if opc < 1 or opc > 3:
    print("\033[1;31mERRO:\033[m\033[31m Opção incorreta!\033[m")
else:
    vetNPC = ['Pedra','Papel','Tesoura']
    respNPC = choice(vetNPC)
    if opc == 1:
        opc = vetNPC[0]
    elif opc == 2:
        opc = vetNPC[1]
    else:
        opc = vetNPC[2]
    
    if opc == 'Pedra':
        emoUsr = ':rock:'
    elif opc == 'Tesoura':
        emoUsr = ':scissors:'
    else:
        emoUsr = ':page_with_curl:'
 	
    if respNPC == 'Pedra':
        emoNPC = ':rock:'
    elif respNPC == 'Tesoura':
        emoNPC = ':scissors:'
    else:
        emoNPC = ':page_with_curl:'

    print(emojize("\033[35mJO\033[m :rock:", language="alias"))
    sleep(1)
    print(emojize("\033[33mKEN\033[m :page_with_curl:", language="alias"))
    sleep(1)
    print(emojize("\033[32mPÔ!!!\033[m :scissors:", language="alias"))
    sleep(1)
    print()
    print("=-" * 50)
    print(emojize("\033[33m- Voce escolheu {} {}\033[m".format(opc,emoUsr), language="alias"))
    print(emojize("\033[33m- Eu escolhi {} {}\033[m".format(respNPC,emoNPC), language="alias"))
    print("=-" * 50)
    if respNPC == 'Pedra' and opc == 'Pedra' or respNPC == 'Papel' and opc == 'Papel' or respNPC == 'Tesoura' and opc == 'Tesoura':
        print(emojize("Empatamos :neutral_face:", language="alias"))
    elif respNPC == 'Tesoura' and opc == 'Pedra' or respNPC == 'Papel' and opc == 'Tesoura' or respNPC == 'Pedra' and opc == 'Papel':
        print(emojize("\033[36m* Você venceu! :confused: \033[m", language="alias"))
    else:
        print(emojize("\033[32m* Eu venci :stuck_out_tongue_winking_eye: \033[m", language="alias"))
print()