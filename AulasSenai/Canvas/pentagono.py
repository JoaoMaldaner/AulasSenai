import tkinter as tk
from tkinter import Canvas

janela = tk.Tk()

janela.title("Pentágono")
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="yellow")
canvas.pack()

canvas.create_polygon(
    110, 50,    # topo
    167, 92,    # direita superior
    145, 160,   # direita inferior
    75, 160,    # esquerda inferior
    53, 92,     # esquerda superior
    fill="blue",
    outline="black",
    width=3
)

janela.mainloop()