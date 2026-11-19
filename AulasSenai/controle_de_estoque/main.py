
# Controle de estoque - Empresa de informática

import json
import os

arquivo = "estoque.json"

# CARREGAR ESTOQUE
def carregar_estoque():

    if not os.path.exists(arquivo):
        return []

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError:
        return []


# SALVAR ESTOQUE
def salvar_dados(estoque):

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii=False, indent=4)


# GERAR ID
def obter_id(estoque):

    if not estoque:
        return 1

    return max(int(item["id"]) for item in estoque) + 1


# ADICIONAR PRODUTO
def adicionar_produto():

    estoque = carregar_estoque()

    nome = input("Digite o nome do produto: ").strip()

    if not nome:
        print("Nome inválido.")
        return

    # Verificar se o produto já existe
    for produto in estoque:

        if produto["nome"].strip().lower() == nome.lower():

            print("Produto já cadastrado.")

            while True:
                try:
                    quantidade = int(input("Quantidade a adicionar: "))

                    if quantidade < 1:
                        print("Digite pelo menos 1 unidade.")
                        continue

                    break

                except ValueError:
                    print("Digite um número inteiro.")

            produto["quantidade"] += quantidade

            salvar_dados(estoque)

            print("Estoque atualizado com sucesso!")
            return

    # Cadastro de novo produto
    novo_id = obter_id(estoque)

    while True:
        try:
            quantidade = int(input("Quantidade inicial: "))

            if quantidade < 5:
                print("Quantidade mínima inicial é 5 unidades.")
                continue

            break

        except ValueError:
            print("Digite um número inteiro.")

    fornecedor = input("Nome do fornecedor: ").strip()

    while True:
        try:
            preco = float(input("Preço do produto: R$ ").replace(",", "."))

            if preco < 0:
                print("Preço inválido.")
                continue

            break

        except ValueError:
            print("Digite um preço válido.")

    novo_produto = {
        "id": novo_id,
        "nome": nome,
        "fornecedor": fornecedor,
        "preco": preco,
        "quantidade": quantidade
    }

    estoque.append(novo_produto)

    salvar_dados(estoque)

    print("Produto cadastrado com sucesso!")


# LISTAR PRODUTOS
def listar_produtos():

    estoque = carregar_estoque()

    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    print("\n========== ESTOQUE ==========")

    for produto in estoque:

        print(f"\nID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Fornecedor: {produto['fornecedor']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']} unidades")

        if produto["quantidade"] <= 5:
            print("ATENÇÃO: Estoque no limite mínimo!")

    print("\n=============================")


# EXCLUIR PRODUTO
def excluir_produto():

    estoque = carregar_estoque()

    if not estoque:
        print("Nenhum produto cadastrado.")
        return

    listar_produtos()

    try:
        id_excluir = int(input("\nDigite o ID para excluir: "))

    except ValueError:
        print("ID inválido.")
        return

    for produto in estoque:

        if produto["id"] == id_excluir:

            estoque.remove(produto)

            salvar_dados(estoque)

            print("Produto excluído com sucesso!")
            return

    print("Produto não encontrado.")


#Saida de estoque 

def saida_e():

    estoque = carregar_estoque

    if not estoque:
        print("Nenhum produto cadastrado")
        return
    


# MENU PRINCIPAL
def menu():

    while True:

        print("\n===== CONTROLE DE ESTOQUE =====")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Excluir produto")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            excluir_produto()

        elif opcao == "4":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
