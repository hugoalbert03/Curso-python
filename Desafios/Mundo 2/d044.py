from time import sleep
print("{:=^90}".format("\033[1;33m Gerenciador de Pagamentos \033[m"))
print("")
val = float(input("\033[1;36mPreço das Compras:\033[m\033[32m R$"))
print("\033[m")
if val <= 0:
    print("Valor inválido")
else:
    print('''\033[35m
    Escolha uma forma de pagamento:

    [1] À vista (Dinheiro/Cheque)
    [2] Cartão\033[m
    ''')
    op = int(input("\033[1;33mOpção:\033[m\033[36m "))
    print("\033[m")
    if op < 1 or op > 2:
        print("\033[5;31mOPÇÃO INVÁLIDA DE PAGAMENTO!\033[m")
    else:
        if op == 1:
            prc = 10/100
            vPrc = val * prc    
            desc = val - vPrc
            print("\033[35mCarregando...\033[m")
            print()
            sleep(2)
            print("\033[36mSeu valor de \033[1;33mR${:.2f}\033[m\033[36m em dinheiro com\033[m\033[35m 10%\033[m \033[36mde desconto vai custar\033[m\033[1;32m R${:.2f}\033[m".format(val,desc))
            print()
        else:            
            print('''\033[32m
    Quais opções você deseja pagar no cartão?

    [1] Pagar à vista
    [2] Em até 2x
    [3] 3x ou Mais
            \033[m''')
            op2 = int(input("\033[1;33mOpção: \033[m\033[36m"))
            print("\033[m")
            if op2 < 0 or op2 > 3:
                print("\033[5;31mOPÇÃO INVÁLIDA!\033[m")
            else:
                if op2 == 1:
                    prc2 = 5/100
                    vPrc2 = val * prc2
                    desc2 = val - vPrc2
                    print("\033[35mCarregando...\033[m")
                    sleep(2)
                    print()
                    print("\033[36m- Seu valor de \033[m\033[1;33mR${:.2f}\033[m\033[36m à vista no cartão com desconto de\033[m\033[35m 5%\033[m\033[36m é \033[m\033[1;32mR${:.2f}\033[m".format(val,desc2))
                elif op2 == 2:
                    pcDiv = val / 2
                    print("\033[35mCarregando...\033[m")
                    sleep(2)
                    print()
                    print("\033[36m- Seu valor dividido\033[m\033[1;33m 2x\033[m\033[36m no cartão é\033[m\033[1;32m R${:.2f}\033[m\033[36m sem juros.\033[m".format(pcDiv))
                    print("\033[36m- Sua compra de\033[m \033[1;32mR${:.2f}\033[m\033[36m vai custar\033[m\033[1;32m R${:.2f}\033[m \033[36mno final\033[m.".format(val,val))
                    print()
                else:
                    vParc = int(input("\033[1;36mDeseja parcelar em quantas vezes? :\033[m\033[32m "))
                    print("\033[m")
                    if vParc < 3 or vParc > 12:
                        print("\033[1;31mERRO:\033[m\033[31m As parcelas nesta opção devem ser entre 3 a 12 vezes!\033[m")
                    else:
                        vprc = val * 20/100
                        tot = val + vprc
                        pcl = tot / vParc
                        print("\033[35mCarregando...\033[m")
                        sleep(2)
                        print()
                        print("\033[36m- Seu valor dividido em\033[m\033[1;33m {}x\033[m\033[36m com \033[m\033[1;31m20%\033[m\033[36m de juros é \033[m\033[1;32mR${:.2f}\033[m".format(vParc,pcl))
                        print("\033[36m- O valor atual de\033[m\033[1;32m R${:.2f}\033[m\033[36m será\033[m\033[1;33m R${:.2f}\033[m\033[36m com juros.\033[m".format(val,tot))
                        print()