from math import sqrt, floor

num = int(input("Digite um número: "));

raizq = sqrt(num);

print("A raiz quadrada de {} é igual à {:.2f}".format(num,floor(raizq)))