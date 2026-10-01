import os
import re
import tkinter as tk
from tkinter import messagebox
import main 
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
                    # users[usuario] = (senha, cpf, saldo)
                    users[p[0]] = (p[1], p[2], float(p[3]))
    return users

def salvar_user(u, s, c, saldo):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{u};{s};{c};{saldo}\n")

def checar_senha(s):
    if len(s) < 8:
        return False, "Mínimo de 8 caracteres."
    if not re.search(r"[a-z]", s):
        return False, "Falta letra minúscula."
    if not re.search(r"[A-Z]", s):
        return False, "Falta letra maiúscula."
    if not re.search(r"\d", s):
        return False, "Falta número."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", s):
        return False, "Falta caractere especial."
    return True, ""

def validar_cpf(cpf):
    #remove caracteres não numéricos (caso o usuário digite com pontos ou traço)
    cpf = re.sub(r'\D', '', cpf)

    #verifica se tem 11 dígitos ou se todos os números são iguais (ex: "11111111111")
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    #validação do 1º dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        return False

    #validação do 2º dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    if digito2 != int(cpf[10]):
        return False

    return True

def tela_cad(antiga):
    antiga.destroy()
    
    jan = tk.Tk()
    jan.title("Cadastro")
    jan.geometry("600x700")
    jan.resizable(False, False)
    jan.configure(bg=branco)

    f = tk.Frame(jan, bg=branco)
    f.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(f, text="Criar Conta", font=("Arial", 20, "bold"), fg=verde_escuro, bg=branco).pack(pady=20)

    tk.Label(f, text="Usuário", font=("Arial", 14), fg=verde_escuro, bg=branco).pack()
    e_user = tk.Entry(f, font=("Arial", 14), justify="center")
    e_user.pack(pady=5)

    tk.Label(f, text="Senha", font=("Arial", 14), fg=verde_escuro, bg=branco).pack()
    e_senha = tk.Entry(f, font=("Arial", 14), show="*", justify="center")
    e_senha.pack(pady=5)

    tk.Label(f, text="CPF", font=("Arial", 14), fg=verde_escuro, bg=branco).pack()
    e_cpf = tk.Entry(f, font=("Arial", 14), justify="center")
    e_cpf.pack(pady=5)

    tk.Label(f, text="Saldo inicial R$ 1000,00", font=("Arial", 14), fg=verde_escuro, bg=branco).pack(pady=5)

    def cadastrar():
        u = e_user.get().strip()
        s = e_senha.get().strip()
        c = e_cpf.get().strip()
        saldo = 1000.00
        
        if not u or not s or not c:
            messagebox.showerror("Erro", "Preencha tudo!")
            return

        users = ler_users()
        
        if u in users:
            messagebox.showerror("Erro", "Usuário já existe!")
            return
            
        #verifica se o CPF já existe varrendo os valores do dicionário
        cpfs_cadastrados = [dados[1] for dados in users.values()]
        if c in cpfs_cadastrados:
            messagebox.showerror("Erro", "CPF já cadastrado!")
            return

        ok, msg = checar_senha(s)
        if not ok:
            messagebox.showerror("Aviso", msg)
            return

        if not validar_cpf(c):
            messagebox.showerror("Erro", "CPF inválido!")
            return


        salvar_user(u, s, c, saldo)
        messagebox.showinfo("Sucesso", "Cadastrado!")
        jan.destroy()
        tela_login()

    tk.Button(f, text="Cadastrar", font=("Arial", 14), bg=verde_escuro, fg=branco, command=cadastrar, width=15).pack(pady=15)
    tk.Button(f, text="Voltar", font=("Arial", 12), bg=cinza, command=lambda: [jan.destroy(), tela_login()], width=15).pack()

    jan.mainloop()

#criando a tela de login
def tela_login():
    jan = tk.Tk()
    jan.title("Login")
    jan.geometry("600x700")
    jan.resizable(False, False)
    jan.configure(bg=branco)

    f = tk.Frame(jan, bg=branco)
    f.place(relx=0.5, rely=0.5, anchor="center")

    try:
        img = tk.PhotoImage(file="semfundo.png").subsample(3, 3)
        lbl_img = tk.Label(f, image=img, bg=branco)
        lbl_img.image = img
        lbl_img.pack(pady=10)
    except:
        pass

    tk.Label(f, text="Usuário", font=("Arial", 14), fg=verde_escuro, bg=branco).pack()
    e_user = tk.Entry(f, font=("Arial", 14), justify="center")
    e_user.pack(pady=5)

    tk.Label(f, text="Senha", font=("Arial", 14), fg=verde_escuro, bg=branco).pack()
    e_senha = tk.Entry(f, font=("Arial", 14), show="*", justify="center")
    e_senha.pack(pady=5)

    #função para logar o usuário
    def logar():
        u = e_user.get().strip()
        s = e_senha.get().strip()

        if not u or not s:
            messagebox.showerror("Erro", "Preencha tudo!")
            return

        users = ler_users()
        # users[u][0] pega a senha armazenada naquela tupla
        if u in users and users[u][0] == s:
            messagebox.showinfo("Sucesso", f"Logado, {u}!")
            jan.destroy()
            main.abrir_menu(u)  # Abre o seu main.py passando o nome do usuário
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    tk.Button(f, text="Entrar", font=("Arial", 14), bg=verde_escuro, fg=branco, command=logar, width=15).pack(pady=15)
    tk.Button(f, text="Criar Conta", font=("Arial", 12), bg=azul_claro, command=lambda: tela_cad(jan), width=15).pack()

    jan.mainloop()

if __name__ == "__main__":
    tela_login()