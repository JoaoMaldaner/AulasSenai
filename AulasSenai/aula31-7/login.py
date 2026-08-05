import tkinter as tk
root = tk.Tk()
root.title("Frames aula 31-7")
root.geometry("320x480")
#root.config(bg="#0C2FA1")

tk.Label(root, text="Faça seu login", font="arial 32 bold").pack(ipady=5, fill="x")  # fill="x" faz com que o widget ocupe toda a largura disponível, e ipady adiciona um preenchimento interno vertical para aumentar a altura do widget.

userImage = tk.PhotoImage(file="images.png").subsample(1, 1)  # subsample(2, 2) reduz a imagem para metade do tamanho original em ambas as dimensões (largura e altura).

label = tk.Label(root, image=userImage, relief=tk.SUNKEN, bd=2)  # relief=tk.SUNKEN cria um efeito de relevo afundado ao redor do widget, e bd=2 define a largura da borda em 2 pixels.
label.pack(expand=True)

tk.Label(root, text="Usuário").pack(anchor=tk.W, padx=20) #ancor=tk.W significa que o widget será ancorado à esquerda (West) do seu contêiner pai. Isso faz com que o widget seja posicionado à esquerda, independentemente do tamanho do contêiner.
user = tk.Entry(root)
user.pack()

tk.Label(root, text="Senha").pack(anchor=tk.W, padx=20)
password = tk.Entry(root, show="*")
password.pack()

botao = tk.Button(root, text="Login")
botao.pack(pady=10)





tk.Checkbutton(root, text="Lembrar-me").pack(side=tk.LEFT, padx=20, pady=5)
tk.Label(root, text="Esqueceu sua senha?", fg="blue", cursor="hand2").pack(side=tk.RIGHT, padx=20, pady=5)


root.mainloop()

