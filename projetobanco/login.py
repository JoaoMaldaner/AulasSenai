import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


branco = "#ffffff"
preto = "#000000"
laranja = "#fcc058"
amarelo = "#fff873"
verde = "#34eb3d"
vermelho = "#e85151"
cinza = "#b3afaf"
azul = "#2500fa"
verde_escuro = "#2e7d32"
verde_claro = "#81c784"
azul_claro = "#64b5f6"

#def login():





janela = tk.Tk()
janela.title("Login")
janela.geometry("800x920")
janela.resizable(False, False)

frame_login = tk.Frame(janela, bg=branco)
frame_login.pack(expand=True, fill="both", padx=20, pady=20)


logoImage = tk.PhotoImage(file="/home/maldaner/AulasSenai/projetobanco/images/semfundo.png").subsample(3, 3)
logo_label = tk.Label(frame_login, image=logoImage, bg=branco)
logo_label.grid(row=0, column=1, columnspan=4, pady=20, sticky="nsew") 


usuario_label = tk.Label(frame_login, text="Usuário", font=("Arial", 20, "bold"), fg=verde_escuro, bg=branco)
usuario_label.grid(row=1, column=1, pady=10) 

usuario_entry = tk.Entry(frame_login, font=("Arial", 14), bg=branco, fg=verde_escuro)
usuario_entry.grid(row=1, column=2, pady=10) 

senha_label = tk.Label(frame_login, text="Senha", font=("Arial", 20, "bold"), fg=verde_escuro, bg=branco)
senha_label.grid(row=2, column=1, pady=10) 
senha_entry = tk.Entry(frame_login, font=("Arial", 14), show="*", bg=branco, fg=verde_escuro)
senha_entry.grid(row=2, column=2, pady=10) 

botao_login = tk.Button(frame_login, text="Login", font=("Arial", 14), bg=verde_escuro, fg=branco)
botao_login.grid(row=3, column=2, columnspan=1, pady=20, sticky="nsew") 


janela.mainloop()