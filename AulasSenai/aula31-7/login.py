import tkinter as tk
root = tk.Tk()
root.title("Frames aula 31-7")
root.geometry("600x600")
#root.config(bg="#0C2FA1")

tk.Label(root, text="Faça seu login").pack(ipady=50)  # fill="x" faz com que o widget ocupe toda a largura disponível, e ipady adiciona um preenchimento interno vertical para aumentar a altura do widget.

userImage = tk.PhotoImage(file="images.png")  # Certifique-se de que o caminho para a imagem esteja correto

label = tk.Label(root, image=userImage)
label.pack(expand=True)

tk.Label(root, text="Usuário").pack(anchor=tk.W) #ancor=tk.W significa que o widget será ancorado à esquerda (West) do seu contêiner pai. Isso faz com que o widget seja posicionado à esquerda, independentemente do tamanho do contêiner.
user = tk.Entry(root)
user.pack()

tk.Label(root, text="Senha").pack(anchor=tk.W)
password = tk.Entry(root, show="*")
password.pack()

botao = tk.Button(root, text="Login")
botao.pack(pady=10)





tk.Checkbutton(root, text="Lembrar-me").pack(side=tk.LEFT)
tk.Label(root, text="Esqueceu sua senha?").pack(side=tk.RIGHT)


root.mainloop()


