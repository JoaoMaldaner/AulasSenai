import tkinter as tk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")

#Ler o título da janela
title = root.title()

#Criar rótulo (label)com o título da janela
message = tk.Label(root, text=title)
teste = tk.Label(root, text="Teste")

#Posiciona o rótulo na janela
message.pack()
teste.pack()

#define o tamanho da janela (largura x altura + posição x, posição y)
root.geometry("400x200+50+250")

root.mainloop()
