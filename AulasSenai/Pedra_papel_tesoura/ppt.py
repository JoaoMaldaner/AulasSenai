import tkinter as tk
from tkinter import ttk

#cores

cor0 = "#FFFFFF" #branco
cor1 = "#000000" #preto
cor2 = "#fcc058" #laranja
cor3 = "#fff873" #amarelo
cor4 = "#34eb3d" #verde
cor5 = "#e85151" #vermelho
fundo = "#3b3b3b" #cinza

janela = tk.Tk()
janela.title("Pedra, Papel e Tesoura")
janela.geometry("260x280")
janela.configure(bg=fundo)

def jogar(escolha):
    import random
    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_computador = random.choice(opcoes)

    if escolha == escolha_computador:
        resultado = "Empate!"
    elif (escolha == "Pedra" and escolha_computador == "Tesoura") or (escolha == "Papel" and escolha_computador == "Pedra") or (escolha == "Tesoura" and escolha_computador == "Papel"):
        resultado = "Você venceu!"
    else:
        resultado = "Você perdeu!" 

    label_resultado.config(text=f"Você escolheu: {escolha}\nComputador escolheu: {escolha_computador}\nResultado: {resultado}")

tk.Label(janela, text="Escolha uma opção:", bg=fundo, fg=cor0, font=("Arial", 12)).pack(pady=10)
tk.Button(janela, text="Pedra", command=lambda: jogar("Pedra"), bg=cor2, fg=cor1, font=("Arial", 12)).pack(pady=5)
tk.Button(janela, text="Papel", command=lambda: jogar("Papel"), bg=cor3, fg=cor1, font=("Arial", 12)).pack(pady=5)
tk.Button(janela, text="Tesoura", command=lambda: jogar("Tesoura"), bg=cor4, fg=cor1, font=("Arial", 12)).pack(pady=5)
label_resultado = tk.Label(janela, text="", bg=fundo, fg=cor0, font=("Arial", 12))
label_resultado.pack(pady=10)







janela.mainloop()