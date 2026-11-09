#controle de gastos com uso de arquivo .json

import json
import os
import uuid
from datetime import datetime
from pathlib import Path


arquivo = "gastos.json"

def carregar_gastos():
    #carrega o arquivo ou retorna uma lista vazia caso não existir 
    if not os.path.exists(arquivo):
        return []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_dados(gastos):
    #salva os dados no arquivo .json
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=4)



def adicionar_receitas():
    #adiciona uma receita (salario, renda extra, etc) ao arquivo .json
    descricao = input("Digite a descrição da receita: ")
    while True:
        try:
            valor = float(input("Digite o valor da receita: "))
            break
        except ValueError:
            print("Valor inválido. Digite um numero válido. ")

    receita = {
        "id": obter_id(),
        "descricao": descricao,
        "valor": valor,
        "tipo": "receita",
        "data": datetime.now().strftime("%H:%M:%S %d/%m/%Y"),
    }

    gastos = carregar_gastos()
    gastos.append(receita)
    salvar_dados(gastos)

def adicionar_despesas():
    #adiciona uma despesa (alimentação, transporte, etc) ao arquivo .json
    descricao = input("Digite a descrição da despesa: ")
    while True:
        try:
            valor = float(input("Digite o valor da despesa: "))
            break
        except ValueError:
            print("Valor inválido. Digite um numero válido. ")

    despesa = {
        "id": obter_id(),
        "descricao": descricao,
        "valor": valor,
        "tipo": "despesa",
        "data": datetime.now().strftime("%H:%M:%S %d/%m/%Y"),
    }

    gastos = carregar_gastos()
    gastos.append(despesa)
    salvar_dados(gastos)

def excluir_movimentacao():
    #exclui uma movimentação (receita ou despesa) do arquivo .json
    gastos = carregar_gastos()
    if not gastos:
        print("Nenhuma movimentação encontrada.")
        return

    listar_movimetacao()
    while True:
        try:
            id_excluir = int(input("Digite o ID da movimentação que deseja excluir: "))
            break
        except ValueError:
            print("ID inválido. Digite um numero válido. ")

    for gasto in gastos:
        if gasto["id"] == id_excluir:
            gastos.remove(gasto)
            salvar_dados(gastos)
            print("Movimentação excluída com sucesso.")
            return

    print("Movimentação não encontrada.")

def listar_movimetacao():
    #lista todas as movimentações (receitas e despesas) do arquivo .json
    gastos = carregar_gastos()
    if not gastos:
        print("Nenhuma movimentação encontrada.")
        return

    for gasto in gastos:
        print(f"ID: {gasto['id']}")
        print(f"Descrição: {gasto['descricao']}")
        print(f"Valor: R$ {gasto['valor']:.2f}")
        print(f"Tipo: {gasto['tipo']}")
        print(f"Data: {gasto['data']}")
        print("-" * 30)

def calcular_saldo():
    #calcula o saldo atual (receitas - despesas) do arquivo .json
    gastos = carregar_gastos()
    saldo = 0.0
    for gasto in gastos:
        if gasto["tipo"] == "receita":
            saldo += gasto["valor"]
        elif gasto["tipo"] == "despesa":
            saldo -= gasto["valor"]
    return saldo

def exibir_saldo():
    #exibe o saldo atual (receitas - despeas) do arquivo .json
    saldo = calcular_saldo()
    print(f"Saldo atual: R$ {saldo:.2f}")
    #voltar ao menu principal
    return input("Pressione Enter para voltar ao menu principal!")

def obter_id():
    #obtem o id da movimentação para excluir ou editar
    gastos = carregar_gastos()
    if not gastos:
        return 1
    return max(gasto["id"] for gasto in gastos) + 1

def menu():
    #menu principal de controle de gastos 
    while True:
        print("\nControle de Gastos")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Listar Movimentações")
        print("4. Exibir Saldo Atual")
        print("5. Excluir Movimentação")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_receitas()
        elif opcao == "2":
            adicionar_despesas()
        elif opcao == "3":
            listar_movimetacao()
        elif opcao == "4":
            exibir_saldo()
        elif opcao == "5":
            excluir_movimentacao()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()















