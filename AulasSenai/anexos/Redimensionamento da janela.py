#Redimensionamento da janela

import tkinter as tk

root = tk.Tk()

root.geometry("400x300")

root.resizable(True, True)  # Permitir redimensionamento horizontal e vertical

root.minsize(300, 200)  # Tamanho mínimo da janela
root.maxsize(800, 600)  # Tamanho máximo da janela

root.attributes('-alpha', 0.5)  # Definir a transparência da janela (0.0 a 1.0)

root.mainloop()

#0.0 Invisível
#0.5 Semi-transparente
#1.0 Totalmente visível(Opaco/padrão)
