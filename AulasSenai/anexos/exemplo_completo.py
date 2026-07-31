nomes = ["Ana", "Bruno", "Carlos", "Diana"]
with open("nomes.txt", "w", encoding="utf-8") as f:
    for nome in nomes:
        f.write(nome + "\n")

#Sempre prefira WITH OPEN(...)para garantir o fechamento automático.Lembre-se de usar \n nas strings se quiser quebras de linha.Para dados numéricos ou não-textuais, converta com str() antes de escrever.