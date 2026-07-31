import tkinter as tk

# CORREÇÃO: Adicionados os parênteses () para inicializar a janela
root = tk.Tk()
root.title("Minha Interface")

def acao_botao():
    print("Botão clicado!")

# Criar os elementos (widgets)
message = tk.Label(root, text="Hello World!") # Corrigido de Word para World
botao = tk.Button(root, text="Clique aqui", command=acao_botao)

# Posicionar os elementos na ordem correta (Texto primeiro, depois Botão)
message.pack(pady=10)
botao.pack(pady=20)


root.geometry("400x200+50+250")

root.mainloop()
