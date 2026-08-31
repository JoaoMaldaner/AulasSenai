import tkinter as tk
from tkinter import Canvas

janela = tk.Tk()
janela.title("Casa e Carro")
janela.geometry("800x500")

canvas = Canvas(janela, width=800, height=500, bg="skyblue")
canvas.pack()


# CHÃO


canvas.create_rectangle(
    0, 400, 800, 500,
    fill="green"
)


# CASA


# Corpo da casa
canvas.create_rectangle(
    100, 220, 400, 400,
    fill="lightyellow",
    outline="black",
    width=3
)

# Telhado
canvas.create_polygon(
    70, 220,
    250, 80,
    430, 220,
    fill="red",
    outline="black",
    width=3
)

# Porta
canvas.create_rectangle(
    220, 300, 290, 400,
    fill="brown",
    outline="black",
    width=3
)

# Maçaneta
canvas.create_oval(
    270, 345, 280, 355,
    fill="yellow",
    outline="black"
)

# Janela esquerda
canvas.create_rectangle(
    130, 270, 190, 330,
    fill="lightblue",
    outline="black",
    width=3
)

# Cruz da janela esquerda
canvas.create_line(
    160, 270, 160, 330,
    fill="black",
    width=2
)

canvas.create_line(
    130, 300, 190, 300,
    fill="black",
    width=2
)

# Janela direita
canvas.create_rectangle(
    310, 270, 370, 330,
    fill="lightblue",
    outline="black",
    width=3
)

# Cruz da janela direita
canvas.create_line(
    340, 270, 340, 330,
    fill="black",
    width=2
)

canvas.create_line(
    310, 300, 370, 300,
    fill="black",
    width=2
)


# CARRO


# Parte inferior do carro
canvas.create_rectangle(
    480, 330, 700, 390,
    fill="blue",
    outline="black",
    width=3
)

# Parte superior / teto
canvas.create_polygon(
    520, 330,
    555, 280,
    630, 280,
    670, 330,
    fill="blue",
    outline="black",
    width=3
)

# Janela esquerda
canvas.create_polygon(
    555, 325,
    570, 290,
    600, 290,
    600, 325,
    fill="lightblue",
    outline="black"
)

# Janela direita
canvas.create_polygon(
    605, 290,
    625, 290,
    655, 325,
    605, 325,
    fill="lightblue",
    outline="black"
)

# Roda esquerda
canvas.create_oval(
    510, 365, 555, 410,
    fill="black"
)

canvas.create_oval(
    520, 375, 545, 400,
    fill="gray"
)

# Roda direita
canvas.create_oval(
    625, 365, 670, 410,
    fill="black"
)

canvas.create_oval(
    635, 375, 660, 400,
    fill="gray"
)

# Farol
canvas.create_oval(
    680, 340, 695, 355,
    fill="yellow",
    outline="black"
)

# Para-choque
canvas.create_line(
    475, 385, 490, 385,
    fill="black",
    width=5
)

canvas.create_line(
    700, 385, 715, 385,
    fill="black",
    width=5
)

janela.mainloop()