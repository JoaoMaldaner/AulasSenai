nomes = ["Ana", "Bruno", "Carlos"]
with open("saida3.txt", "w") as f:
    for nome in nomes:
        f.write(nome + "\n")
