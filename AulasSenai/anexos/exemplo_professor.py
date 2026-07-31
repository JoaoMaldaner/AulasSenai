print("Digite nomes (pressione Enter para finalizar):")
nomes = []
while True:
    nome = input("Digita um nome:")
    if nome == "":
        break
    nomes.append(nome)

    with open("nomes3.txt", "w", encoding="utf-8") as f:
        for nome in nomes:
            f.write(nome + "\n")

#With open(...) garante o fechamento automático do arquivo. Lembre-se de usar \n nas strings se quiser quebras de linha. Para dados numéricos ou não-textuais, converta com str() antes de escrever.

#Witch open("nomes.txt", "w", encoding="utf-8") as f:
#    conteudo = f.read()
#print(conteudo)
