nomes = []

for i in range(3):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

with open("saida4.txt", "w") as f:
    for nome in nomes:
        f.write(nome + "\n")