import tkinter as tk
from tkinter import ttk, Canvas

janela = tk.Tk()

janela.title("Canvas")
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="yellow")

canvas.create_polygon(100, 50, 150, 150, 50, 150, fill="blue", outline="black", width=2)

canvas.pack()

janela.mainloop()