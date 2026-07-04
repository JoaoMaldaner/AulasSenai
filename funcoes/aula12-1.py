def desenha_linha(limite, preenchimento, largura):
    print(limite + (preenchimento * (largura - 2)) + limite)
def montar_menu(itens, largura):
    for item in itens:
        print('+', '-', largura)
        print(f'| {item:<16} |')
        if item != itens[-1]:
            desenha_linha('+', '-', largura)
    desenha_linha('+', '-', largura)
itens = ["Usuários", "Clientes", "Fornecedores", "Relatórios", "Teste"]
item_largura = 20
montar_menu(itens, item_largura)