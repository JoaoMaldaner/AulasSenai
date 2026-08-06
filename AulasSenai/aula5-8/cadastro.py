import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Frames aula grid")
#root.geometry("320x600")


userImage = tk.PhotoImage(file="images.png").subsample(1, 1)
label = tk.Label(root, image=userImage, relief=tk.SUNKEN, bd=2)
label.grid(row=0, column=0, rowspan=5, padx=5, pady=5)

tk.Label(root, text="Nome:").grid(row=0, column=1, sticky="w", padx=5, pady=5)
tk.Entry(root).grid(row=0, column=2, sticky="ew", padx=5, pady=5)

tk.Label(root, text="Gênero:").grid(row=1, column=1, sticky="w", padx=5, pady=5)
genero = ttk.Combobox(root,values=[ "Masculino", "Feminino", "Outro"], state="readonly")
genero.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

tk.Label(root, text="Cor dos Olhos:").grid(row=2, column=1, sticky="w", padx=5, pady=5)
corOlhos = ttk.Combobox(root,values=[ "Azul", "Verde", "Castanho", "Preto"], state="readonly")
corOlhos.grid(row=2, column=2, sticky="ew",padx=5, pady=5)

tk.Label(root, text="Altura:").grid(row=3, column=1, sticky="w", padx=5, pady=5)
tk.Entry(root).grid(row=3, column=2, sticky="ew", padx=5, pady=5)

tk.Label(root, text="Peso:").grid(row=4, column=1, sticky="w", padx=5, pady=5)
tk.Entry(root).grid(row=4, column=2, sticky="ew",padx=5, pady=5)

tk.Button(root, text="enviar").grid(row=5, column=1, columnspan=2, sticky="e", padx=5, pady=5)







root.mainloop()