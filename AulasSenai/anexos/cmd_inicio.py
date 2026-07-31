import tkinter as tk

#Cria a Janela principal
root = tk.Tk()

#Cria um rótulo (label) com o texto "Sabia que o T-rex possuia a mordida mais poderosa dentre todos os dinossauros"
message = tk.Label(root, text="SABIA QUE O T-REX POSSUIA A MORDIDA MAIS PODEROSA DENTRE TODOS OS DINOSSAUROS?")

#Posiciona o rótulo na janela
message.pack()

#inicia o loop principal da interface gráfica
root.mainloop()
