nomes = []
for i in range(4):
    nome = input("Digita um nome:")
    nomes.append(nome)
with open("nomes2.txt", "w", encoding="utf-8") as f:
    for nome in nomes:
        f.write(nome + "\n")