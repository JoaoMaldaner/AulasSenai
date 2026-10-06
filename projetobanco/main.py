import os
import tkinter as tk
from tkinter import messagebox
import login  

# Cores
branco = "#ffffff"
preto = "#000000"
verde_escuro = "#2e7d32"
cinza = "#b3afaf"
azul_claro = "#64b5f6"
vermelho = "#e85151"

ARQUIVO = "usuarios.txt"

def ler_users(): #definir e buscar o arquivo com os usuarios salvos
    users = {}
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for l in f:
                p = l.strip().split(";")
                if len(p) == 4:
                    # users[usuario] = (senha, cpf, saldo)
                    users[p[0]] = (p[1], p[2], float(p[3]))
    return users

def salvar_todos_usuarios(users):
    #salva o dicionário completo de volta no arquivo txt atualizando os saldos.
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for u, dados in users.items():
            f.write(f"{u};{dados[0]};{dados[1]};{dados[2]:.2f}\n")

# consultar o saldo
def tela_saldo(usuario_logado):
    users = ler_users()
    saldo = users[usuario_logado][2] if usuario_logado in users else 0.0
    messagebox.showinfo("Consulta de Saldo", f"Seu saldo atual é de: R$ {saldo:.2f}")

# função de sacar o dinheiro
def tela_sacar(usuario_logado, janela_menu):
    jan_s = tk.Toplevel(janela_menu)
    jan_s.title("Sacar Dinheiro")
    jan_s.geometry("400x300")
    jan_s.resizable(False, False)
    jan_s.configure(bg=branco)

    f = tk.Frame(jan_s, bg=branco)
    f.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(f, text="Valor do Saque (R$):", font=("Arial", 12, "bold"), fg=verde_escuro, bg=branco).pack(pady=5)
    e_valor = tk.Entry(f, font=("Arial", 14), justify="center")
    e_valor.pack(pady=5)

    def processar_saque():
        val_str = e_valor.get().strip().replace(",", ".") #altera os caracteres de virgula e ponto para aceitar ambos
        try:
            valor = float(val_str)
        except ValueError:
            messagebox.showerror("Erro", "Insira apenas números válidos!", parent=jan_s)
            return

        if valor <= 0:
            messagebox.showerror("Erro", "Não é permitido saque de valores negativos ou zerados!", parent=jan_s)
            return

        if not valor.is_integer():
            messagebox.showerror("Erro", "O caixa eletrônico não trabalha com centavos para saque!", parent=jan_s)
            return

        int_valor = int(valor)

        if int_valor == 1 or int_valor == 3:
            messagebox.showerror("Erro", "O caixa não possui notas para este valor (mínimo R$ 2,00).", parent=jan_s)
            return

        int_valor = int(valor)

        # bloqueia qualquer valor terminado em 1 ou 3. 
        ultimo_digito = int_valor % 10
        if int_valor == 1 or int_valor == 3 or ultimo_digito == 1 or ultimo_digito == 3:
            messagebox.showerror("Erro", "O caixa não possui notas para atender a este valor (valores terminados em 1 ou 3 são impossíveis).", parent=jan_s)
            return

        users = ler_users()
        if usuario_logado in users:
            senha_atual, cpf_atual, saldo_atual = users[usuario_logado]

            if int_valor > saldo_atual:
                messagebox.showerror("Erro", "Saldo insuficiente para realizar este saque!", parent=jan_s)
                return

            restante = int_valor
            n100 = restante // 100
            restante %= 100

            n50 = restante // 50
            restante %= 50

            n20 = restante // 20
            restante %= 20

            n10 = restante // 10
            restante %= 10

            n5 = restante // 5
            restante %= 5

            if restante % 2 != 0:
                n5 -= 1
                restante += 5

            n2 = restante // 2

            novo_saldo = saldo_atual - int_valor
            users[usuario_logado] = (senha_atual, cpf_atual, novo_saldo)
            salvar_todos_usuarios(users)


            #exibir as celulas entregues no saque
            detalhes_cedulas = f"Saque de R$ {int_valor:.2f} realizado com sucesso!\n\nCédulas entregues:\n"
            if n100 > 0: detalhes_cedulas += f"- R$ 100,00: {n100}\n"
            if n50 > 0:  detalhes_cedulas += f"- R$ 50,00: {n50}\n"
            if n20 > 0:  detalhes_cedulas += f"- R$ 20,00: {n20}\n"
            if n10 > 0:  detalhes_cedulas += f"- R$ 10,00: {n10}\n"
            if n5 > 0:   detalhes_cedulas += f"- R$ 5,00: {n5}\n"
            if n2 > 0:   detalhes_cedulas += f"- R$ 2,00: {n2}\n"

            # fecha a janela de saque e mostra a msg com detalhes das cédulas
            jan_s.destroy()
            janela_menu.after(100, lambda: messagebox.showinfo("Sucesso", detalhes_cedulas, parent=janela_menu))

    tk.Button(f, text="Confirmar Saque", font=("Arial", 12), bg=verde_escuro, fg=branco, command=processar_saque, width=15).pack(pady=15)

# função de depositar o dinheiro
def tela_depositar(usuario_logado, janela_menu):
    jan_d = tk.Toplevel(janela_menu)
    jan_d.title("Depositar Dinheiro")
    jan_d.geometry("400x300")
    jan_d.resizable(False, False)
    jan_d.configure(bg=branco)

    f = tk.Frame(jan_d, bg=branco)
    f.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(f, text="Valor do Depósito (R$):", font=("Arial", 12, "bold"), fg=verde_escuro, bg=branco).pack(pady=5)
    e_valor = tk.Entry(f, font=("Arial", 14), justify="center")
    e_valor.pack(pady=5)

    def processar_deposito():
        val_str = e_valor.get().strip().replace(",", ".") #altera os caracteres de virgula e ponto para aceitar ambos
        try:
            valor = float(val_str)
        except ValueError:
            messagebox.showerror("Erro", "Insira um valor numérico válido!", parent=jan_d)
            return

        if valor <= 0:
            messagebox.showerror("Erro", "Não é permitido depositar valores negativos ou zerados!", parent=jan_d) #garante que o valor do depósito seja positivo
            return

        users = ler_users()
        if usuario_logado in users:
            senha_atual, cpf_atual, saldo_atual = users[usuario_logado]
            novo_saldo = saldo_atual + valor

            users[usuario_logado] = (senha_atual, cpf_atual, novo_saldo)
            salvar_todos_usuarios(users)

            # fechar a janela de deposito e mostra a msg com saldo
            jan_d.destroy()
            janela_menu.after(100, lambda: messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso!\nNovo saldo: R$ {novo_saldo:.2f}", parent=janela_menu))

    tk.Button(f, text="Confirmar Depósito", font=("Arial", 12), bg=verde_escuro, fg=branco, command=processar_deposito, width=18).pack(pady=15)

# criando menu principal
def abrir_menu(usuario_logado):
    janela_menu = tk.Tk()
    janela_menu.title("Caixa Eletrônico - Menu Principal")
    janela_menu.geometry("800x600")
    janela_menu.resizable(False, False)
    janela_menu.configure(bg=branco)

    #frame de boas vindas 
    frame_topo = tk.Frame(janela_menu, bg=branco)
    frame_topo.pack(fill="x", padx=20, pady=20)

    try:
        img_logo = tk.PhotoImage(file="logo.png").subsample(5, 5)
        lbl_logo = tk.Label(frame_topo, image=img_logo, bg=branco)
        lbl_logo.image = img_logo  
        lbl_logo.pack(side="left", padx=(0, 15))
    except Exception:
        lbl_logo = tk.Label(frame_topo, text="[Logo]", font=("Arial", 12), bg=branco, fg=cinza)
        lbl_logo.pack(side="left", padx=(0, 15))

    tk.Label(
        frame_topo, 
        text=f"Bem-vindo, {usuario_logado}!", 
        font=("Arial", 18, "bold"), 
        fg=verde_escuro, 
        bg=branco
    ).pack(side="left", anchor="w")

    #criando os botões de operação
    tk.Button(
        janela_menu, text="1. Consultar Saldo", font=("Arial", 12), bg=verde_escuro, fg=branco, width=25,
        command=lambda: tela_saldo(usuario_logado)
    ).pack(pady=10)

    tk.Button(
        janela_menu, text="2. Sacar Dinheiro", font=("Arial", 12), bg=verde_escuro, fg=branco, width=25,
        command=lambda: tela_sacar(usuario_logado, janela_menu)
    ).pack(pady=10)

    tk.Button(
        janela_menu, text="3. Depositar Dinheiro", font=("Arial", 12), bg=verde_escuro, fg=branco, width=25,
        command=lambda: tela_depositar(usuario_logado, janela_menu)
    ).pack(pady=10)

    #sair ou fechar o programa
    def sair_conta():
        if messagebox.askokcancel("Sair", "Deseja encerrar a sessão desta conta?"):
            janela_menu.destroy()
            login.tela_login()

    def encerrar_programa():
        if messagebox.askokcancel("Encerrar", "Deseja fechar todo o programa?"):
            janela_menu.destroy()

    frame_inferior = tk.Frame(janela_menu, bg=branco)
    frame_inferior.pack(side="bottom", pady=40)

    tk.Button(
        frame_inferior, text="4. Sair (Trocar Conta)", font=("Arial", 12), 
        bg=vermelho, fg=branco, width=20, command=sair_conta
    ).pack(side="left", padx=10)

    tk.Button(
        frame_inferior, text="Fechar Programa", font=("Arial", 12), 
        bg=vermelho, fg=branco, width=18, command=encerrar_programa
    ).pack(side="left", padx=10)

    janela_menu.mainloop()

if __name__ == "__main__":
    abrir_menu("Convidado")