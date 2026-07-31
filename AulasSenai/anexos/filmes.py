def menu():
    print("0 - Adicionar filme (opcional")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")

def adicionar_filme():
    print("Adicionar filme:")

def contar_filmes():
    print("Contar filmes:")

def info_por_titulo():
    print("informação por filme:")

def filmes_por_diretor():
    print("Filmes por diretor:")

def filmes_por_genero():
    print("Filme por genero:")

def media_duracao():
    print("Media de duração:")

if __name__ == "__main__":
    while True:
        menu()
        opcao = input("Escolha uma opção:").strip()

        if opcao == "0":
            adicionar_filme()
        elif opcao == "1":
            contar_filmes()
        elif opcao == "2":
            info_por_titulo()
        elif opcao == "3":
            filmes_por_diretor()
        elif opcao == "4":
            filmes_por_genero()
        elif opcao == "5":
            media_duracao()
        elif opcao == "6":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

        