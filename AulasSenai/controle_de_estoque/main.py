#programa para criar um controle de estoque de uma empresa de informatica, cadastro de preços, produtos, fornecedores e quatidade em estoque com um valor mnimo de 5 unidades em cada id criado

#criar o arquivo .json para armazenar os dados
import json
import os

arquivo = "estoque.json"

def carregar_estoque():
    #carrega os dados do arquivo .json
    if not os.path.exists(arquivo):
        return []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_dados(estoque):
    #salva os dados no arquivo .json
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii=False, indent=4)

def obter_id():
    #pega o proximo numero de id
    estoque = carregar_estoque()
    if not estoque:
        return 1
    return max(int(item["id"]) for item in estoque) + 1

def reordenar_ids(estoque):
    #reordena os IDs sequencialmente (1, 2, 3...)
    for indice, item in enumerate(estoque, start=1):
        item["id"] = indice
    return estoque

def adicionar_produto():
    #adiciona um produto ao arquivo .json
    nome = input("Digite o nome do produto: ")
    fornecedor = input("Digite o nome do fornecedor: ")
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            break
        except ValueError:
            print("Valor inválido. Digite um numero válido. ")
    while True:
        try:
            quantidade = int(input("Digite a quantidade em estoque (mínimo 5 unidades): "))
            if quantidade < 5:
                print("Quantidade mínima é de 5 unidades. Digite novamente.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite um numero válido. ")

    produto = {
        "id": obter_id(),
        "nome": nome,
        "fornecedor": fornecedor,
        "preco": preco,
        "quantidade": quantidade
    }

    estoque = carregar_estoque()
    estoque.append(produto)
    salvar_dados(estoque)


def listar_produtos():
    #lista os produtos cadastrados no arquivo .json
    estoque = carregar_estoque()
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    for produto in estoque:
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Fornecedor: {produto['fornecedor']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']} unidades")

def excluir_produto():
    #exclui um produto do arquivo .json
    estoque = carregar_estoque()
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos()
    while True:
        try:
            id_excluir = int(input("Digite o ID do produto que deseja excluir: "))
            break
        except ValueError:
            print("ID inválido. Digite um numero válido. ")

    for produto in estoque:
        if produto["id"] == id_excluir:
            estoque.remove(produto)
            salvar_dados(estoque)
            print("Produto excluído com sucesso.")
            return

    print("Produto não encontrado.")

def adicionar_ao_id_existente():
    #adiciona quantidade a um produto existente no arquivo .json
    estoque = carregar_estoque()
    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos()
    while True:
        try:
            id_adicionar = int(input("Digite o ID do produto que deseja adicionar quantidade: "))
            break
        except ValueError:
            print("ID inválido. Digite um numero válido. ")

    for produto in estoque:
        if produto["id"] == id_adicionar:
            while True:
                try:
                    quantidade_adicionar = int(input("Digite a quantidade que deseja adicionar: "))
                    if quantidade_adicionar <= 0:
                        print("Quantidade deve ser maior que zero. Digite novamente.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido. Digite um numero válido. ")
            produto["quantidade"] += quantidade_adicionar
            salvar_dados(estoque)
            print(f"Quantidade adicionada com sucesso. Novo estoque: {produto['quantidade']} unidades.")
            return

    print("Produto não encontrado.")

    

        






def menu():
    #menu do programa

    while True:
        print("\nControle de Estoque")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Excluir Produto")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
    