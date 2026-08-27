import tkinter as tk 
from tkinter import ttk, Canvas

janela = tk.Tk()
janela.title("Canvas")
janela.geometry("500x400")

canvas = Canvas(janela, width=400, height=300, bg="yellow")

canvas.create_rectangle(50, 50, 150, 100, fill="blue")

canvas.create_oval(200, 50, 300, 150, fill="red")
canvas.create_line(50, 200, 350, 200, fill="green", width=3)


canvas.pack()
janela.mainloop()