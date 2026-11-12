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


#adicinar produto e verificar se o nome do produto ja existe caso ja exista, adiciona no ID do mesmo se não ele cria um novo id
def adicionar_produto(nome):
    estoque = carregar_estoque()
    nome_simples = nome.strip().lower()

    for produto in estoque:
        if produto["nome"].strip().lower() == nome_simples:
            print("Produto já cadastrado. Adicionando quantidade ao produto existente.")
            while True:
                try:
                    quantidade_adicional = int(input("Digite a quantidade a ser adicionada: "))
                    if quantidade_adicional < 0:
                        print("Quantidade inválida. Digite um número positivo.")
                        continue
                    break
                except ValueError:
                    print("Quantidade inválida. Digite um número inteiro.")

            produto["quantidade"] += quantidade_adicional
            salvar_dados(estoque)
            print("Quantidade adicionada com sucesso.")
            return
    novo_id = obter_id()


    qunatidade = input("Digite a quantidade a ser adicionada: ")
    while True:
        try:
            quantidade = int(qunatidade)
            if quantidade < 5:
                print("Quantidade mínima é 5. Definindo quantidade como 5.")
                quantidade = 5
            break
        except ValueError:
            print("Quantidade inválida. Digite um número inteiro.")
            qunatidade = input("Digite a quantidade a ser adicionada: ")

    fornecedor = input("Digite o nome do fornecedor: ")
    preco = input("Digite o preço do produto: ")
    while True:
        try:
            preco = float(preco)
            if preco < 0:
                print("Preço inválido. Digite um número positivo.")
                preco = input("Digite o preço do produto: ")
                continue
            break
        except ValueError:
            print("Preço inválido. Digite um número válido.")
            preco = input("Digite o preço do produto: ")
    novo_produto = {
        "id": novo_id,
        "nome": nome,
        "fornecedor": fornecedor,
        "preco": preco,
        "quantidade": quantidade
    }

    


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
    