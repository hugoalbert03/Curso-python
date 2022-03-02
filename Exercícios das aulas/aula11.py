# Cores no terminal
# 0 é sem formatação
print("\033[1;33;44m Teste \033[m") # 1 é negrito
print()
print("\033[2;33;44m Teste \033[m") # 2 é letras negativas
print()
print("\033[3;33;44m Teste \033[m") # 3 é letras em itálico
print()
print("\033[4;33;44m Teste \033[m") # 4 é letras sublinhadas
print()
print("\033[5;33;44m Teste \033[m") # 5 é letras piscando
print()
print("\033[7;33;44m Teste \033[m") # 7 é inversão de cores
print()
print("\033[8;33;44m Teste \033[m") # 8 é invisibilidade das letras
print()
print("\033[9;33;44m Teste \033[m") # 9 é Letras cortadas

#pesquisar sobre a biblioteca "colorize"
cores = {'amarelo':'\033[33m', 'verde':'\033[32m','limpo':'\033[m'} #Esquematização de cores
print("{} Meu nome é {}{}{}!".format(cores['verde'],cores['amarelo'],"Hugo",cores['limpo']))