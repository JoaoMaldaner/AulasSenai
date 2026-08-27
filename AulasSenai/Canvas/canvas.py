import tkinter as tk 
from tkinter import ttk, Canvas

janela = tk.Tk()
janela.title("Canvas")
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="yellow")

canvas.pack()
janela.mainloop()