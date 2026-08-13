import tkinter as tk
from tkinter import NW, Frame, ttk

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
janela.geometry("260x450")
janela.configure(bg=fundo)

#criar função jogar
def jogar(escolha):
    import random
    opcoes = ["Pedra", "Papel", "Tesoura"]
    escolha_computador = random.choice(opcoes)

    if escolha == escolha_computador:
        resultado = "Empate!"
        app_pontos_empate["text"] = str(int(app_pontos_empate["text"]) + 1)
    elif (escolha == "Pedra" and escolha_computador == "Tesoura") or (escolha == "Papel" and escolha_computador == "Pedra") or (escolha == "Tesoura" and escolha_computador == "Papel"):
        resultado = "Você venceu!"
        app_pontos_pessoa["text"] = str(int(app_pontos_pessoa["text"]) + 1)
    else:
        resultado = "Você perdeu!" 
        app_pontos_computador["text"] = str(int(app_pontos_computador["text"]) + 1)

    label_resultado.config(text=f"Você escolheu: {escolha}\nComputador escolheu: {escolha_computador}\nResultado: {resultado}")



frame_cima = Frame(janela, width=260, height=100, bg=cor1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=300, bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)
frame_empate = Frame(janela, width=260, height=50, bg=cor3, relief="flat")
frame_empate.grid(row=2, column=0, sticky=NW)

#COnfigurando jogadores

#jogador pessoa 

app_pessoa = tk.Label(frame_cima, text="Jogador", height=1, anchor="center", font=("Ivy 10 bold"), bg=cor1, fg=cor0)
app_pessoa.place(x=10, y=70)
#marcando a pontuação do jogador
app_pessoa_linha   = tk.Label(frame_cima, text="", height=10, anchor="center", font=("Ivy 10 bold"), bg=cor4, fg=cor0)
app_pessoa_linha.place(x=0, y=0)

# pontuação do pessoa

app_pontos_pessoa = tk.Label(frame_cima, text="0", height=1, anchor="center", font=("Ivy 30 bold"), bg=cor1, fg=cor0)
app_pontos_pessoa.place(x=50, y=20) 

#separador
app_separador = tk.Label(frame_cima, text=":", height=1, anchor="center", font=("Ivy 30 bold"), bg=cor1, fg=cor0)
app_separador.place(x=125, y=20)

# joador computador

app_computador = tk.Label(frame_cima, text="Computador", height=1, anchor="center", font=("Ivy 10 bold"), bg=cor1, fg=cor0)
app_computador.place(x=165, y=70)
#definindo linha do computador
app_computador_linha   = tk.Label(frame_cima, text="", height=10, anchor="center", font=("Ivy 10 bold"), bg=cor5, fg=cor0)
app_computador_linha.place(x=255, y=0)

#pontuação do computador

app_pontos_computador = tk.Label(frame_cima, text="0", height=1, anchor="center", font=("Ivy 30 bold"), bg=cor1, fg=cor0)
app_pontos_computador.place(x=180, y=20)

app_empate = tk.Label(frame_empate, text="Empates", height=1, anchor="center", font=("Ivy 10 bold"), bg=cor3, fg=cor1)
app_empate.place(x=10, y=10)
app_pontos_empate = tk.Label(frame_empate, text="0", height=1, anchor="center", font=("Ivy 30 bold"), bg=cor3, fg=cor1)
app_pontos_empate.place(x=100, y=-5)

#criar botao de ação com imagem

imagem_pedra = tk.PhotoImage(file="pedra.png").subsample(8, 6)
botao_pedra = tk.Button(frame_baixo, image=imagem_pedra, width=50, height=50, bg=cor0, relief="flat", overrelief="solid")
botao_pedra.place(x=20, y=20)

imagem_papel = tk.PhotoImage(file="papel.png").subsample(8, 6)
botao_papel = tk.Button(frame_baixo, image=imagem_papel, width=50, height=50, bg=cor0, relief="flat", overrelief="solid")
botao_papel.place(x=100, y=20)

imagem_tesoura = tk.PhotoImage(file="tesoura.png").subsample(8, 6)
botao_tesoura = tk.Button(frame_baixo, image=imagem_tesoura, width=50, height=50, bg=cor0, relief="flat", overrelief="solid")
botao_tesoura.place(x=180, y=20)

#seleção de ação jogador seleciona uma opção e o computador seleciona uma opção aleatória
botao_pedra.config(command=lambda: jogar("Pedra"))
botao_papel.config(command=lambda: jogar("Papel"))
botao_tesoura.config(command=lambda: jogar("Tesoura"))





#resultado
label_resultado = tk.Label(frame_baixo, text="", height=3, anchor="center", font=("Ivy 10 bold"), bg=cor0, fg=cor1)
label_resultado.place(x=20, y=100)







janela.mainloop()