import os
import re
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

def ler_users():
    users = {}
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for l in f:
                p = l.strip().split(";")
                if len(p) == 4:
                    users[p[0]] = (p[1], p[2], float(p[3]))
    return users

def abrir_menu(usuario_logado):
    janela_menu = tk.Tk()
    janela_menu.title("Menu Principal")
    janela_menu.geometry("800x600")
    janela_menu.resizable(False, False)
    janela_menu.configure(bg=branco)

    #alinhar a logo e o texto de buenas
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
        text=f"Buenas, {usuario_logado}!", 
        font=("Arial", 18, "bold"), 
        fg=verde_escuro, 
        bg=branco
    ).pack(side="left", anchor="w")

    # Botões centrais do menu
    tk.Button(janela_menu, text="Ver Saldo", font=("Arial", 12), bg=verde_escuro, fg=branco, command=lambda: consultar_saldo(usuario_logado), width=20).pack(pady=10)
    tk.Button(janela_menu, text="Sacar", font=("Arial", 12), bg=verde_escuro, fg=branco, command=lambda: jan_sacar(usuario_logado), width=20).pack(pady=10)
    tk.Button(janela_menu, text="Depositar", font=("Arial", 12), bg=verde_escuro, fg=branco, command=lambda: jan_depositar(usuario_logado), width=20).pack(pady=10)

    def voltar_login():
        janela_menu.destroy()
        login.tela_login()

    def encerrar_programa():
        if messagebox.askokcancel("Sair", "Deseja realmente sair do programa?"):
            janela_menu.destroy()

    # Frame inferior para os botões de deslogar e sair (usando pack para evitar o erro)
    frame_inferior = tk.Frame(janela_menu, bg=branco)
    frame_inferior.pack(side="bottom", pady=40)

    tk.Button(
        frame_inferior, text="Deslogar", font=("Arial", 12), 
        bg=vermelho, fg=branco, width=15, command=voltar_login
    ).pack(side="left", padx=10)

    tk.Button(
        frame_inferior, text="Encerrar Programa", font=("Arial", 12), 
        bg=vermelho, fg=branco, width=15, command=encerrar_programa
    ).pack(side="left", padx=10)

    janela_menu.mainloop()

def consultar_saldo(usuario):
    users = ler_users()
    if usuario in users:
        saldo = users[usuario][2]
        messagebox.showinfo("Saldo", f"Seu saldo é: R$ {saldo:.2f}")
    else:
        messagebox.showerror("Erro", "Usuário não encontrado.")

def jan_sacar(usuario_logado):
    jan = tk.Tk()
    jan.title("Saque")
    jan.geometry("400x300")
    jan.resizable(False, False)
    jan.configure(bg=branco)

    f = tk.Frame(jan, bg=branco)
    f.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(f, text="Valor do Saque", font=("Arial", 14), fg=verde_escuro, bg=branco).pack()
    e_valor = tk.Entry(f, font=("Arial", 14), justify="center")
    e_valor.pack(pady=5)

    def sacar():
        valor = e_valor.get().strip()
        if not valor:
            messagebox.showerror("Erro", "Preencha o valor!")
            return
        try:
            valor = float(valor)
            if valor <= 0:
                messagebox.showerror("Erro", "Valor inválido!")
                return
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido!")
            return

        users = ler_users()
        if usuario_logado in users:
            saldo_atual = users[usuario_logado][2]
            if valor > saldo_atual:
                messagebox.showerror("Erro", "Saldo insuficiente!")
                return
            else:
                users[usuario_logado] = (users[usuario_logado][0], users[usuario_logado][1], saldo_atual - valor)
                with open(ARQUIVO, "w", encoding="utf-8") as f:
                    for u, dados in users.items():
                        f.write(f"{u};{dados[0]};{dados[1]};{dados[2]:.2f}\n")

        messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado com sucesso!")
        jan.destroy()
    tk.Button(f, text="Sacar", font=("Arial", 12), bg=verde_escuro, fg=branco, command=sacar, width=15).pack(pady=15)









#rodar direto o main.py para testes, abre com um usuário padrão
if __name__ == "__main__":
    abrir_menu("Convidado")

