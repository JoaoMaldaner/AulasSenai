filmes = []
ARQUIVO = "filmes.txt"

def adicionar_filme():
    titulo = input("Título: ")
    ano = input("Ano: ")
    diretor = input("Diretor: ")
    genero = input("Gênero: ")
    duracao = input("Duração (min): ")

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{titulo};{ano};{diretor};{genero};{duracao}\n")

    print("Filme cadastrado com sucesso!")



def menu():
    print("++ MENU ++")
    print("0 - Adicionar um Filme")
    print("1 - Quantidade total de filmes")
    print("2 - Informações do filme pelo título")
    print("3 - Filmes de um diretor especifico")
    print("4 - Filmes de um gênero especifico")
    print("5 - Média de duração dos Filmes")


