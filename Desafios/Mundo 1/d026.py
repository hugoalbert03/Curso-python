f = str(input("Digite uma frase: ")).lower().strip()
print('A letra "a" aparece {} vez(es) na frase.'.format(f.count("a")))
print('A primeira vez que a letra "A" aparece é na posição {}'.format(f.find('a') + 1))
print('A última letra "A" aparece na posição {}'.format(f.rfind('a') + 1))