import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def sair(event=None):
    """Função para fechar a aplicação"""
    jan.destroy()

jan = tk.Tk()
jan.title("Sistema Bancário")
jan.geometry("800x600")
jan.resizable(False, False)

# Textos do sistema
tk.Label(jan, text="Sistema Bancário", font=("Arial", 24, "bold"), fg="#2E8B57").pack(pady=20)
tk.Label(jan, text="para sair pressione Enter", font=("Arial", 12), fg="#555555").pack(pady=10)

# Botão de ação (corrigido para incluir o 'jan' como primeiro argumento)
button = ttk.Button(jan, text="Pressione Enter ou clique aqui", command=sair)
button.pack(pady=10)

# Associa a tecla <Return> (Enter) da janela para chamar a função de sair
jan.bind("<Return>", sair)

# Foca na janela para garantir que o evento de teclado funcione imediatamente
jan.focus_set()

jan.mainloop()