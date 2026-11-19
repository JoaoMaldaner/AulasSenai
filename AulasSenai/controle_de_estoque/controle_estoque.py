import json
import os
from datetime import datetime
from decimal import Decimal, InvalidOperation

ARQUIVO_PRODUTOS = "estoque.json"
ARQUIVO_MOVIMENTACOES = "movimentacoes.json"


def carregar_json(caminho):
    """Carrega um arquivo JSON. Se não existir, inicia uma lista vazia."""
    if not os.path.exists(caminho):
        return []

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            if not isinstance(dados, list):
                raise ValueError("O conteúdo do arquivo deve ser uma lista.")
            return dados
    except (json.JSONDecodeError, OSError, ValueError) as erro:
        print(f"\nErro ao carregar {caminho}: {erro}")
        print("O sistema continuará com uma lista vazia em memória.")
        return []


def salvar_json(caminho, dados):
    """Salva os dados em JSON, evitando deixar um arquivo incompleto."""
    temporario = caminho + ".tmp"
    try:
        with open(temporario, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        os.replace(temporario, caminho)
    except OSError as erro:
        print(f"\nNão foi possível salvar {caminho}: {erro}")
        try:
            if os.path.exists(temporario):
                os.remove(temporario)
        except OSError:
            pass


def ler_inteiro(mensagem, minimo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Informe um número maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_preco(mensagem):
    while True:
        try:
            texto = input(mensagem).strip().replace(",", ".")
            valor = Decimal(texto)
            if not valor.is_finite() or valor <= 0:
                print("O preço deve ser um número maior que zero.")
                continue
            return float(valor)
        except (InvalidOperation, ValueError):
            print("Preço inválido. Exemplo: 79,90")


def buscar_codigo(produtos, codigo):
    for produto in produtos:
        if produto.get("codigo") == codigo:
            return produto
    return None


def pausar():
    input("\nPressione ENTER para continuar...")


def mostrar_produto(produto):
    print(
        f"Código: {produto['codigo']} | "
        f"Nome: {produto['nome']} | "
        f"Quantidade: {produto['quantidade']} | "
        f"Mínimo: {produto['estoque_minimo']} | "
        f"Preço: R$ {produto['preco']:.2f}"
    )


def cadastrar_produto(produtos):
    print("\n--- CADASTRAR PRODUTO ---")
    codigo = ler_inteiro("Código: ", 1)

    if buscar_codigo(produtos, codigo):
        print("Já existe um produto cadastrado com esse código.")
        return

    nome = input("Nome do produto: ").strip()
    if not nome:
        print("O nome do produto é obrigatório.")
        return

    quantidade = ler_inteiro("Quantidade inicial: ", 0)
    estoque_minimo = ler_inteiro("Estoque mínimo: ", 0)
    preco = ler_preco("Preço unitário (R$): ")

    produtos.append({
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "estoque_minimo": estoque_minimo,
        "preco": preco
    })
    salvar_json(ARQUIVO_PRODUTOS, produtos)
    print("Produto cadastrado com sucesso.")


def listar_produtos(produtos):
    print("\n--- LISTA DE PRODUTOS ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'CÓDIGO':<10}{'PRODUTO':<30}{'QTD.':>8}{'MÍNIMO':>10}{'PREÇO':>14}")
    print("-" * 72)
    for produto in sorted(produtos, key=lambda item: item["codigo"]):
        print(
            f"{produto['codigo']:<10}"
            f"{produto['nome'][:28]:<30}"
            f"{produto['quantidade']:>8}"
            f"{produto['estoque_minimo']:>10}"
            f"R$ {produto['preco']:>9.2f}"
        )


def alterar_produto(produtos):
    print("\n--- ALTERAR PRODUTO ---")
    codigo = ler_inteiro("Código do produto: ", 1)
    produto = buscar_codigo(produtos, codigo)

    if not produto:
        print("Produto não encontrado.")
        return

    mostrar_produto(produto)
    print("\nDeixe o campo vazio para manter o valor atual.")

    nome = input(f"Nome [{produto['nome']}]: ").strip()
    if nome:
        produto["nome"] = nome

    while True:
        texto = input(f"Quantidade [{produto['quantidade']}]: ").strip()
        if not texto:
            break
        try:
            valor = int(texto)
            if valor < 0:
                print("A quantidade não pode ser negativa.")
                continue
            produto["quantidade"] = valor
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    while True:
        texto = input(f"Estoque mínimo [{produto['estoque_minimo']}]: ").strip()
        if not texto:
            break
        try:
            valor = int(texto)
            if valor < 0:
                print("O estoque mínimo não pode ser negativo.")
                continue
            produto["estoque_minimo"] = valor
            break
        except ValueError:
            print("Digite um número inteiro válido.")

    while True:
        texto = input(f"Preço [{produto['preco']:.2f}]: ").strip()
        if not texto:
            break
        try:
            valor = Decimal(texto.replace(",", "."))
            if not valor.is_finite() or valor <= 0:
                print("O preço deve ser maior que zero.")
                continue
            produto["preco"] = float(valor)
            break
        except InvalidOperation:
            print("Preço inválido.")

    salvar_json(ARQUIVO_PRODUTOS, produtos)
    print("Produto atualizado com sucesso.")


def excluir_produto(produtos):
    print("\n--- EXCLUIR PRODUTO ---")
    codigo = ler_inteiro("Código do produto: ", 1)
    produto = buscar_codigo(produtos, codigo)

    if not produto:
        print("Produto não encontrado.")
        return

    mostrar_produto(produto)
    confirmacao = input("Confirma a exclusão? (s/n): ").strip().lower()
    if confirmacao == "s":
        produtos.remove(produto)
        salvar_json(ARQUIVO_PRODUTOS, produtos)
        print("Produto excluído.")
    else:
        print("Exclusão cancelada.")


def registrar_movimentacao(produtos, movimentacoes, tipo):
    titulo = "ENTRADA" if tipo == "entrada" else "SAÍDA"
    print(f"\n--- REGISTRAR {titulo} ---")

    if not produtos:
        print("Cadastre um produto antes de registrar movimentações.")
        return

    codigo = ler_inteiro("Código do produto: ", 1)
    produto = buscar_codigo(produtos, codigo)

    if not produto:
        print("Produto não encontrado.")
        return

    mostrar_produto(produto)
    quantidade = ler_inteiro("Quantidade da movimentação: ", 1)

    if tipo == "saida" and quantidade > produto["quantidade"]:
        print("Operação não permitida: a saída é maior que o estoque atual.")
        return

    if tipo == "entrada":
        produto["quantidade"] += quantidade
    else:
        produto["quantidade"] -= quantidade

    movimentacoes.append({
        "tipo": tipo,
        "codigo_produto": produto["codigo"],
        "nome_produto": produto["nome"],
        "quantidade": quantidade,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    })

    salvar_json(ARQUIVO_PRODUTOS, produtos)
    salvar_json(ARQUIVO_MOVIMENTACOES, movimentacoes)
    print(f"{titulo.capitalize()} registrada com sucesso.")
    print(f"Estoque atual de {produto['nome']}: {produto['quantidade']}")


def consultar_produto(produtos):
    print("\n--- CONSULTAR PRODUTO ---")
    print("1 - Consultar por código")
    print("2 - Consultar por nome")
    opcao = input("Escolha: ").strip()

    if opcao == "1":
        codigo = ler_inteiro("Código: ", 1)
        produto = buscar_codigo(produtos, codigo)
        if produto:
            mostrar_produto(produto)
        else:
            print("Produto não encontrado.")

    elif opcao == "2":
        nome = input("Digite o nome ou parte do nome: ").strip().casefold()
        if not nome:
            print("Digite um nome para pesquisar.")
            return
        encontrados = [
            produto for produto in produtos
            if nome in produto["nome"].casefold()
        ]
        if encontrados:
            for produto in encontrados:
                mostrar_produto(produto)
        else:
            print("Nenhum produto encontrado.")
    else:
        print("Opção inválida.")


def produtos_estoque_baixo(produtos):
    print("\n--- PRODUTOS COM ESTOQUE BAIXO ---")
    baixos = [
        produto for produto in produtos
        if produto["quantidade"] <= produto["estoque_minimo"]
    ]

    if not baixos:
        print("Não há produtos com estoque baixo.")
        return

    print(f"{'PRODUTO':<30}{'QUANTIDADE':>14}{'MÍNIMO':>12}")
    print("-" * 56)
    for produto in baixos:
        print(
            f"{produto['nome'][:28]:<30}"
            f"{produto['quantidade']:>14}"
            f"{produto['estoque_minimo']:>12}"
        )


def relatorio_estoque(produtos):
    print("\n--- RELATÓRIO DE ESTOQUE ---")
    listar_produtos(produtos)

    valor_total = sum(
        produto["quantidade"] * produto["preco"] for produto in produtos
    )
    total_itens = sum(produto["quantidade"] for produto in produtos)
    print("-" * 72)
    print(f"Total de unidades em estoque: {total_itens}")
    print(f"Valor estimado do estoque: R$ {valor_total:.2f}")


def relatorio_movimentacoes(movimentacoes):
    print("\n--- HISTÓRICO DE MOVIMENTAÇÕES ---")
    if not movimentacoes:
        print("Nenhuma movimentação registrada.")
        return

    for mov in movimentacoes:
        tipo = mov["tipo"].upper()
        print(
            f"{mov['data']} | {tipo:<7} | "
            f"Cód. {mov['codigo_produto']} | "
            f"{mov['nome_produto']} | Quantidade: {mov['quantidade']}"
        )


def menu():
    produtos = carregar_json(ARQUIVO_PRODUTOS)
    movimentacoes = carregar_json(ARQUIVO_MOVIMENTACOES)

    while True:
        print("\n" + "=" * 42)
        print("       SISTEMA DE CONTROLE DE ESTOQUE")
        print("=" * 42)
        print("1  - Cadastrar produto")
        print("2  - Listar produtos")
        print("3  - Alterar produto")
        print("4  - Excluir produto")
        print("5  - Registrar entrada")
        print("6  - Registrar saída")
        print("7  - Consultar produto")
        print("8  - Produtos com estoque baixo")
        print("9  - Relatório de estoque")
        print("10 - Histórico de movimentações")
        print("0  - Sair")
        print("-" * 42)

        opcao = input("Selecione uma opção: ").strip()

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            alterar_produto(produtos)
        elif opcao == "4":
            excluir_produto(produtos)
        elif opcao == "5":
            registrar_movimentacao(produtos, movimentacoes, "entrada")
        elif opcao == "6":
            registrar_movimentacao(produtos, movimentacoes, "saida")
        elif opcao == "7":
            consultar_produto(produtos)
        elif opcao == "8":
            produtos_estoque_baixo(produtos)
        elif opcao == "9":
            relatorio_estoque(produtos)
        elif opcao == "10":
            relatorio_movimentacoes(movimentacoes)
        elif opcao == "0":
            print("\nSistema encerrado. Dados salvos em JSON.")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")

        pausar()


if __name__ == "__main__":
    menu()
