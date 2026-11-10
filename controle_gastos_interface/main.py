import json
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

arquivo = "gastos_i.json"


# carregar o arquivo com os dados
def carregar_gastos():
    if not os.path.exists(arquivo):
        return []
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


# salvar as informacoes no arquivo
def salvar_dados(gastos):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(gastos, f, ensure_ascii=False, indent=4)


# pegar o proximo numero de id
def obter_id():
    gastos = carregar_gastos()
    if not gastos:
        return 1
    return max(int(gasto["id"]) for gasto in gastos) + 1


# reordenar os IDs sequencialmente (1, 2, 3...)
def reordenar_ids(gastos):
    for indice, item in enumerate(gastos, start=1):
        item["id"] = indice
    return gastos


# somar as receitas e subtrair as despesas
def calcular_saldo():
    gastos = carregar_gastos()
    saldo = 0.0
    for gasto in gastos:
        if gasto["tipo"] == "receita":
            saldo += gasto["valor"]
        elif gasto["tipo"] == "despesa":
            saldo -= gasto["valor"]
    return saldo


# remove um gasto pelo ID do arquivo JSON e reorganiza a sequencia de IDs
def excluir_gasto(id_gasto):
    gastos = carregar_gastos()
    gastos_filtrados = [g for g in gastos if g["id"] != id_gasto]
    gastos_reordenados = reordenar_ids(gastos_filtrados)
    salvar_dados(gastos_reordenados)


# abrir a janela para cadastrar receita ou despesa
def janela_adicionar(tipo, atualizar_tela=None):
    janela = tk.Toplevel()
    janela.title(f"Adicionar {tipo.capitalize()}")
    janela.geometry("300x200")
    janela.resizable(False, False)

    # trava a janela principal enquanto essa estiver aberta
    janela.grab_set()

    tk.Label(janela, text="Descrição:").pack(pady=(10, 0))
    entry_descricao = tk.Entry(janela, width=30)
    entry_descricao.pack(pady=5)
    entry_descricao.focus_set()

    tk.Label(janela, text="Valor (R$):").pack(pady=(5, 0))
    entry_valor = tk.Entry(janela, width=30)
    entry_valor.pack(pady=5)

    def salvar():
        descricao = entry_descricao.get().strip()
        valor_str = entry_valor.get().strip().replace(",", ".")

        if not descricao:
            messagebox.showwarning(
                "Aviso", "A descrição não pode estar vazia.", parent=janela
            )
            return

        try:
            valor = float(valor_str)
            if valor <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Erro",
                "Insira um valor numérico válido e maior que zero.",
                parent=janela,
            )
            return

        novo_item = {
            "id": obter_id(),
            "descricao": descricao,
            "valor": valor,
            "tipo": tipo,
            "data": datetime.now().strftime("%H:%M:%S %d/%m/%Y"),
        }

        gastos = carregar_gastos()
        gastos.append(novo_item)
        salvar_dados(gastos)

        messagebox.showinfo(
            "Sucesso",
            f"{tipo.capitalize()} adicionada com sucesso!",
            parent=janela,
        )

        janela.destroy()

        if atualizar_tela:
            atualizar_tela()

    tk.Button(
        janela,
        text="Salvar",
        width=15,
        command=salvar,
        bg="#4CAF50",
        fg="white",
    ).pack(pady=15)


# abrir a janela com o historico de registros
def janela_listar(atualizar_tela=None):
    janela = tk.Toplevel()
    janela.title("Histórico de Movimentações")
    janela.geometry("600x400")

    janela.grab_set()

    colunas = ("id", "descricao", "valor", "tipo", "data")
    tabela = ttk.Treeview(janela, columns=colunas, show="headings")

    tabela.heading("id", text="ID")
    tabela.heading("descricao", text="Descrição")
    tabela.heading("valor", text="Valor (R$)")
    tabela.heading("tipo", text="Tipo")
    tabela.heading("data", text="Data")

    tabela.column("id", width=40, anchor="center")
    tabela.column("descricao", width=180)
    tabela.column("valor", width=80, anchor="e")
    tabela.column("tipo", width=80, anchor="center")
    tabela.column("data", width=140, anchor="center")

    def carregar_tabela():
        # Limpa itens existentes na tabela
        for item in tabela.get_children():
            tabela.delete(item)

        gastos = carregar_gastos()
        for item in gastos:
            tabela.insert(
                "",
                tk.END,
                values=(
                    item["id"],
                    item["descricao"],
                    f"R$ {item['valor']:.2f}",
                    item["tipo"].capitalize(),
                    item["data"],
                ),
            )

    carregar_tabela()

    scrollbar = ttk.Scrollbar(janela, orient=tk.VERTICAL, command=tabela.yview)
    tabela.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tabela.pack(expand=True, fill=tk.BOTH, padx=10, pady=(10, 0))

    def acao_excluir():
        item_selecionado = tabela.selection()
        if not item_selecionado:
            messagebox.showwarning(
                "Aviso", "Selecione um item para excluir.", parent=janela
            )
            return

        # Pega os valores da linha selecionada
        valores = tabela.item(item_selecionado[0], "values")
        id_gasto = int(valores[0])
        descricao = valores[1]

        confirmacao = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Deseja realmente excluir '{descricao}'?",
            parent=janela,
        )

        if confirmacao:
            excluir_gasto(id_gasto)
            carregar_tabela()  # Atualiza a lista exibida com os novos IDs

            # Atualiza o saldo no menu principal
            if atualizar_tela:
                atualizar_tela()

            messagebox.showinfo(
                "Sucesso", "Movimentação excluída e IDs atualizados!", parent=janela
            )

    # Botão de Excluir
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(fill=tk.X, padx=10, pady=10)

    btn_excluir = tk.Button(
        frame_botoes,
        text="Excluir Selecionado",
        command=acao_excluir,
        bg="#f44336",
        fg="white",
    )
    btn_excluir.pack(side=tk.RIGHT)


# abrir a janela com o relatorio financeiro (total receitas, despesas e saldo)
def janela_relatorio():
    gastos = carregar_gastos()

    total_receitas = sum(g["valor"] for g in gastos if g["tipo"] == "receita")
    total_despesas = sum(g["valor"] for g in gastos if g["tipo"] == "despesa")
    saldo = total_receitas - total_despesas

    janela = tk.Toplevel()
    janela.title("Relatório Financeiro")
    janela.geometry("320x220")
    janela.resizable(False, False)
    janela.grab_set()

    tk.Label(
        janela, text="Resumo de Movimentações", font=("Arial", 14, "bold")
    ).pack(pady=(15, 10))

    frame_info = tk.Frame(janela)
    frame_info.pack(pady=5, padx=15, fill=tk.X)

    # Receitas
    tk.Label(frame_info, text="Total de Receitas:", font=("Arial", 11)).grid(
        row=0, column=0, sticky="w", pady=4
    )
    tk.Label(
        frame_info,
        text=f"R$ {total_receitas:.2f}",
        font=("Arial", 11, "bold"),
        fg="green",
    ).grid(row=0, column=1, sticky="e", padx=(20, 0), pady=4)

    # Despesas
    tk.Label(frame_info, text="Total de Despesas:", font=("Arial", 11)).grid(
        row=1, column=0, sticky="w", pady=4
    )
    tk.Label(
        frame_info,
        text=f"R$ {total_despesas:.2f}",
        font=("Arial", 11, "bold"),
        fg="red",
    ).grid(row=1, column=1, sticky="e", padx=(20, 0), pady=4)

    # Divisor simples
    ttk.Separator(frame_info, orient="horizontal").grid(
        row=2, column=0, columnspan=2, sticky="ew", pady=8
    )

    # Saldo
    cor_saldo = "green" if saldo >= 0 else "red"
    tk.Label(frame_info, text="Saldo Líquido:", font=("Arial", 11, "bold")).grid(
        row=3, column=0, sticky="w", pady=4
    )
    tk.Label(
        frame_info,
        text=f"R$ {saldo:.2f}",
        font=("Arial", 11, "bold"),
        fg=cor_saldo,
    ).grid(row=3, column=1, sticky="e", padx=(20, 0), pady=4)

    tk.Button(
        janela, text="Fechar", width=15, command=janela.destroy
    ).pack(pady=15)


# montar e exibir a janela principal
def janela_principal():
    menu = tk.Tk()
    menu.title("Controle de Gastos")
    menu.geometry("350x400")
    menu.resizable(False, False)

    tk.Label(menu, text="Controle de Gastos", font=("Arial", 16, "bold")).pack(
        pady=15
    )

    label_saldo = tk.Label(menu, text="", font=("Arial", 12))
    label_saldo.pack(pady=(0, 10))

    def atualizar_saldo_label():
        saldo = calcular_saldo()
        cor = "green" if saldo >= 0 else "red"
        label_saldo.config(text=f"Saldo Atual: R$ {saldo:.2f}", fg=cor)

    atualizar_saldo_label()

    tk.Button(
        menu,
        text="Adicionar Receita",
        width=25,
        command=lambda: janela_adicionar("receita", atualizar_saldo_label),
    ).pack(pady=5)
    tk.Button(
        menu,
        text="Adicionar Despesa",
        width=25,
        command=lambda: janela_adicionar("despesa", atualizar_saldo_label),
    ).pack(pady=5)
    tk.Button(
        menu,
        text="Listar Movimentações",
        width=25,
        command=lambda: janela_listar(atualizar_saldo_label),
    ).pack(pady=5)
    tk.Button(
        menu,
        text="Relatório Financeiro",
        width=25,
        command=janela_relatorio,
    ).pack(pady=5)
    tk.Button(
        menu,
        text="Atualizar Saldo",
        width=25,
        command=atualizar_saldo_label,
    ).pack(pady=5)
    tk.Button(
        menu, text="Sair", width=25, command=menu.destroy, fg="red"
    ).pack(pady=12)

    menu.mainloop()


if __name__ == "__main__":
    janela_principal()