#programa para criar um controle de estoque de uma empresa de informatica, cadastro de preços, produtos e fornecedores

#criar o arquivo .json para armazenar os dados
import json
import os

arquivo = "estoque.json"

if not os.path.exists(arquivo):
    with open(arquivo, "w") as f:
        json.dump([], f)