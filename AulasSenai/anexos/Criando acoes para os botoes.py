#Criando ações para os botões

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

def button_command():
    messagebox.showinfo("Informação", "Você clicou no botão!")

button = tk.Button(root, text="Clique aqui", command=button_command)
button.pack(pady=20)

def button_command2():
    messagebox.showwarning("Aviso", "Você clicou no segundo botão!")

button2 = tk.Button(root, text="Clique aqui", command=button_command2)
button2.pack(pady=20)


root.mainloop()

#Como funciona?

#1-Defina a função:Crie uma função que será executada quando o botão for clicado. No exemplo acima, a função button_command() exibe uma mensagem de informação usando messagebox.showinfo().

#2-Vincule com command:Passe o nome da função(sem parênteses)ao botão usando o parâmetro command. Isso garante que a função seja chamada quando o botão for clicado.

#3-Exiba mensagens:Use messagebox para feedback ao usuário. Existem diferentes tipos de caixas de mensagem, como showinfo(), showwarning() e showerror(), dependendo do tipo de informação que você deseja exibir.
