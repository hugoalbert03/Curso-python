from random import shuffle
print("{:=^80}".format("Apresentação de Trabalho"));
a1 = str(input("Nome do Primeiro Aluno: "))
a2 = str(input("Nome do Segundo Aluno: "))
a3 = str(input("Nome do Terceiro Aluno: "))
a4 = str(input("Nome do Quarto Aluno: "))
seq = [a1,a2,a3,a4]
# print("A ordem de alunos para a apresentação do trabalho será \n {}".format(sorted(seq)))
shuffle(seq)
print("A ordem de apresentação será {}".format(seq))