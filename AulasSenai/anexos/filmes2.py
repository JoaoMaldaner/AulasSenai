def contar_filmes():
    contador = 0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            for linha in f:
                if linha.strip().startswith("Título:"):
                    contador += 1
    except FileNotFoundError:
        print("Arquivo' filmes.txt' não encontrado.")
    return 0

    print(f"Quantidade total de filmes: {contador}")
    return contador



def info_por_titulo():
    titulo_busca = input("Título: ").strip().lower().lower()
    encontrado = False
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            for linha in f:
                if linha.strip().startswith("Título:"):
                    titulo = linha.split(":", 1)[1].strip()
                    if titulo.lower() == titulo_busca:
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
        print("Arquivo 'filmes.txt' não encontrado.")
        return
    if not encontrado:
        print("Filme não encontrado.")



def filmes_por_diretor():
    diretor_busca = input("Diretor: ").strip().lower()
    contador = 0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            ultimo_diretor = ""
            for linha in f:
                s = linha.strip()
                if s.startswith("Título:"):
                    ultimo_titulo = s.split(":", 1)[1].strip()
                elif s.startswith("Diretor:"):
                    diretor = s.split(":", 1)[1].strip()
                    if diretor.lower() == diretor_busca:
                        contador += 1
                        print(f"- {ultimo_titulo}")
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado.")
        return
    print(f"Total de filmes do diretor '{diretor_busca}': {contador}")


    
def filmes_por_genero():
    genero_busca = input("Gênero: ").strip().lower()
    contador = 0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            ultimo_titulo = ""
            for linha in f:
                s = linha.strip()
                if s.startswith("Título:"):
                    ultimo_titulo = s.split(":", 1)[1].strip()
                elif s.startswith("Gênero:"):
                    genero = s.split(":", 1)[1].strip()
                    if genero.lower() == genero_busca:
                        contador += 1
                        print(f"- {ultimo_titulo}")
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado.")
        return
    print(f"Total de filmes do gênero '{genero_busca}': {contador}")
    


def filmes_por_duracao():
    soma = 0
    contador = 0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            for linha in f:
                s = linha.strip()
                if s.startswith("Duração:"):
                    duracao_str = s.split(":", 1)[1].strip()
                    try:
                        minutos = int(s.split(":", 1)[1].strip().split()[0])
                    except (ValueError, IndexError):
                        #Ignorar valores inválidos
                        continue
                    soma += minutos
                    contador =+ 1
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado.")
        return

    if contador == 0:
        print("Nenhum filme com duração válida encontrado.")
    else:
        media = soma / contador
        print(f"Média de duração dos filmes: {media:.2f} minutos")
        return media



def filmes_por_ano():
    ano_busca = input("Ano: ").strip().lower()
    contador = 0
    try:
        with open("filmes.txt", encoding="utf-8") as f:
            ultimo_titulo = ""
            for linha in f:
                s = linha.strip()
                if s.startswith("Título:"):
                    ultimo_titulo = s.split(":", 1)[1].strip()
                elif s.startswith("Ano:"):
                    ano: s.split(":", 1)[1].strip()
                    if ano.lower() == ano_busca:
                        contador += 1
                        print(f"- {ultimo_titulo}")
    except FileNotFoundError:
        print("Arquivo 'filmes.txt' não encontrado.")
        return
    print(f"Total de filmes do ano '{ano_busca}': {contador}")



def adicionar_filme():
    titulo = input("Título: ").strip()
    ano = input("Ano: ").strip()
    diretor = input("Diretor: ").strip()
    genero = input("Gênero: ").strip()
    duracao = input("Duração (em minutos): ").strip()

    with open("filmes.txt", "a", encoding="utf-8") as f:
        f.write(f"Título: {titulo}\n")
        f.write(f"Ano: {ano}\n")
        f.write(f"Diretor: {diretor}\n")
        f.write(f"Gênero: {genero}\n")
        f.write(f"Duração: {duracao} minutos\n")
        f.write("\n")  # Adiciona uma linha em branco entre os filmes
    print(f"Filme '{titulo}' adicionado com sucesso.")


while True:
    print("0 - Adicionar filme (opcional")
    print("1 - Quantidade total de filmes")
    print("2 - Informações de um filme pelo título")
    print("3 - Filmes de um diretor específico")
    print("4 - Filmes de um gênero específico")
    print("5 - Média de duração dos filmes")
    print("6 - Sair")


        
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
