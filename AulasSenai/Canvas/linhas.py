import tkinter as tk
from tkinter import ttk, Canvas

janela = tk.Tk()

janela.title("Canvas")
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="yellow")

# Horizontal
canvas.create_line(10, 10, 300, 10, fill="red", width=5)

# Vertical
canvas.create_line(10, 10, 10, 250, fill="blue", width=5)

# Diagonal
canvas.create_line(10, 10, 200, 200, fill="green", width=5)

canvas.pack()

janela.mainloop()