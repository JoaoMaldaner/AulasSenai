import tkinter as tk

#Cria a Janela principal
root = tk.Tk()

#Cria um rótulo (label) com o texto "Hello, World!"
message = tk.Label(root, text="Hello, World!")

#Posiciona o rótulo na janela
message.pack()

#inicia o loop principal da interface gráfica
root.mainloop()