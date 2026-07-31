linhas = ["linha 1 \n", "linha 2 \n", "linha 3 \n"]
with open("saida2.txt", "w") as f:
    f.writelines(linhas)