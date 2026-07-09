with open ("arquivos.txt", "r") as f:
    linhas =  f.readlines()
    for linha in linhas:
        print(linha.strip())