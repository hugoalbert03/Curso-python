nome = str(input("Nome do aluno: "));
n1 = float(input("Primeira nota: "));
n2 = float(input("Segunda nota: "));
print("A media final entre {:.1f} e {:.1f} do aluno {} é de {:.1f} pontos.".format(n1,n2,nome,(float((n1+n2)/2))))