def menu():
    print("0 - Adicionar filme")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")


def adicionar_filme():
    print("Adicionar filme:")
 
def contar_filmes():
    contador = 0
    try:
        with open("filmes.txt", "r" encoding="utf-8 \n") as f:
            for linha in f:
                if linha.strip().startswith("Título:"):
                    contador += 1
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado.")
        return 0
    
    print(f"Quantidade total de filmes: {contador}")
    return contador


def info_por_titulo():
    titulo_busca = input("Título:").strip().lower()
    encontrado = False
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            for linha in f:
                titulo = linha.split(":", 1)[1].strip()
                if linha.strip().startswith("Título:"):
                    print(f"Título: {titulo}")
                    try:
                        ano = next(f).strip()
                        diretor = next(f).strip()
                        genero = next(f).strip()
                        duracao = next(f).strip()
                    except StopIteration:
                        print("Registro incompleto para esse título.")
                        return
                    print(ano)
                    print(diretor)
                    print(genero)
                    print(duracao)
                    encontrado = True
                    break

                    except FileNotFoundError:
                        print("Arquivo ' filmes.txt' não encontrado.")
                        return
                
                    if not encontrado:
                        print("Filme não encontrado.")


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

        print("")    

        
        
    