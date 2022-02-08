from random import randint
nomes = [input("Aluno 1: "),input("Aluno 2: "),input("Aluno 3: "), input("Aluno 4: ")]
sort = nomes[randint(0,3)]
print("O aluno sorteado para apagar o quadro foi {}!".format(sort))