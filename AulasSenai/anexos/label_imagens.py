import tkinter as tk

root = tk.Tk()  
root.title("SENAI - Sistemas")
root.geometry("800x600")

minha_imagem = tk.PhotoImage(file="python.png")  # Certifique-se de que o caminho para a imagem esteja correto

label = tk.Label(root, image=minha_imagem)
label.pack(expand=True)

root.mainloop()
