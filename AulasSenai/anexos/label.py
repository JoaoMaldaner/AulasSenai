import tkinter as tk

root = tk.Tk()

label_1 = tk.Label(root, text="Olá")
label_1.pack()

label_2 = tk.Label(root)
label_2.pack()
label_2.config(text="Definido depois")

label_3 = tk.Label(root, text="Olá", font=("Helvetica", 30))
label_3.pack(expand=True)

root.mainloop()