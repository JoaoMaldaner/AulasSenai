import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600")

spinbox_var = tk.StringVar(value="0")

spinbox = tk.Spinbox(
    root,
    from_=-10,
    to=10,
    #increment=0.5,
    textvariable=spinbox_var
)

spinbox.pack(expand=True)

label = tk.Label(root, textvariable=spinbox_var)
label.pack()

root.mainloop()