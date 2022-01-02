prod = float(input("Digite o preço de um produto: R$"));
perc = prod/100 * 5
print("");
print("{:-^70}".format("Resultado"));
print("");
print("O valor do produto de R${} com 5{} de desconto é igual à R${:.2f}".format(prod,("%"),(prod-perc)));