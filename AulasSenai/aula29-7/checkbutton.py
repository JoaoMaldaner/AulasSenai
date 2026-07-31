import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600")

cb_estado = tk.IntVar()

def mostrar_estado():
    if cb_estado.get():
        txt = "Checked"
    else:
        txt = "Unchecked"

    checkbox.config(text=f"Check me! ({txt})")


checkbox = tk.Checkbutton(
    root,
    text="Check me! (Unchecked)",
    variable=cb_estado,
    command=mostrar_estado
)

checkbox.select()      # Marca o checkbox inicialmente
mostrar_estado()       # Atualiza o texto
checkbox.pack(expand=True)

root.mainloop()