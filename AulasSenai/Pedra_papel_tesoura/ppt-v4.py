import tkinter as tk
from tkinter import Frame
import random

from PIL import Image, ImageTk


# =========================================================
# CORES
# =========================================================

cor0 = "#FFFFFF"       # branco
cor1 = "#000000"       # preto
cor2 = "#fcc058"       # laranja
cor3 = "#fff873"       # amarelo
cor4 = "#34eb3d"       # verde
cor5 = "#e85151"       # vermelho

fundo = "#3b3b3b"

azul_jogador = "#3498DB"
roxo_computador = "#8E44AD"

cinza_linha = "#555555"


# =========================================================
# JANELA
# =========================================================

janela = tk.Tk()

janela.title("Pedra, Papel e Tesoura")

janela.geometry("260x550")

janela.configure(
    bg=fundo
)

janela.resizable(
    False,
    False
)


# =========================================================
# VARIÁVEIS
# =========================================================

escolha_jogador = None
escolha_computador = None

rodada_atual = 0

total_rodadas = 5

pontos_jogador = 0
pontos_computador = 0
pontos_empate = 0


# =========================================================
# FUNÇÃO CARREGAR IMAGEM
# =========================================================

def carregar_imagem(nome):

    imagem = Image.open(nome)

    imagem = imagem.resize(
        (50, 50),
        Image.LANCZOS
    )

    return ImageTk.PhotoImage(imagem)


# =========================================================
# IMAGENS
# =========================================================

imagem_pedra = carregar_imagem(
    "pedra.png"
)

imagem_papel = carregar_imagem(
    "papel.png"
)

imagem_tesoura = carregar_imagem(
    "tesoura.png"
)


# =========================================================
# FRAME DO PLACAR
# =========================================================

frame_cima = Frame(
    janela,
    width=260,
    height=100,
    bg=cor1
)

frame_cima.grid(
    row=0,
    column=0
)

frame_cima.grid_propagate(False)


# =========================================================
# FRAME PRINCIPAL
# =========================================================

frame_baixo = Frame(
    janela,
    width=260,
    height=450,
    bg=cor0
)

frame_baixo.grid(
    row=1,
    column=0
)

frame_baixo.grid_propagate(False)


# =========================================================
# PLACAR - JOGADOR
# =========================================================

app_pessoa = tk.Label(
    frame_cima,
    text="Jogador",
    font=("Ivy", 10, "bold"),
    bg=cor1,
    fg=cor0
)

app_pessoa.place(
    x=10,
    y=70
)


app_pessoa_linha = tk.Label(
    frame_cima,
    width=1,
    height=10,
    bg=cor4
)

app_pessoa_linha.place(
    x=0,
    y=0
)


app_pontos_pessoa = tk.Label(
    frame_cima,
    text="0",
    font=("Ivy", 30, "bold"),
    bg=cor1,
    fg=cor0
)

app_pontos_pessoa.place(
    x=50,
    y=20
)


# =========================================================
# SEPARADOR
# =========================================================

app_separador = tk.Label(
    frame_cima,
    text=":",
    font=("Ivy", 30, "bold"),
    bg=cor1,
    fg=cor0
)

app_separador.place(
    x=125,
    y=20
)


# =========================================================
# COMPUTADOR
# =========================================================

app_computador = tk.Label(
    frame_cima,
    text="Computador",
    font=("Ivy", 10, "bold"),
    bg=cor1,
    fg=cor0
)

app_computador.place(
    x=165,
    y=70
)


app_computador_linha = tk.Label(
    frame_cima,
    width=1,
    height=10,
    bg=cor5
)

app_computador_linha.place(
    x=255,
    y=0
)


app_pontos_computador = tk.Label(
    frame_cima,
    text="0",
    font=("Ivy", 30, "bold"),
    bg=cor1,
    fg=cor0
)

app_pontos_computador.place(
    x=180,
    y=20
)


# =========================================================
# CONFIGURAÇÃO DAS RODADAS
# =========================================================

label_rodadas = tk.Label(
    frame_baixo,
    text="RODADAS",
    font=("Ivy", 9, "bold"),
    bg=cor0,
    fg=cor1
)

label_rodadas.place(
    x=15,
    y=5
)


# ---------------------------------------------------------
# SPINBOX
# ---------------------------------------------------------

spin_rodadas = tk.Spinbox(
    frame_baixo,
    from_=1,
    to=99,
    increment=2,
    width=5,
    justify="center",
    font=("Ivy", 11, "bold")
)

spin_rodadas.delete(
    0,
    "end"
)

spin_rodadas.insert(
    0,
    "5"
)

spin_rodadas.place(
    x=80,
    y=2
)


# =========================================================
# FUNÇÃO VALIDAR RODADAS
# =========================================================

def validar_rodadas():

    global total_rodadas

    try:

        valor = int(
            spin_rodadas.get()
        )

        # Não permite zero ou negativo
        if valor < 1:

            raise ValueError

        # Só permite números ímpares
        if valor % 2 == 0:

            label_config.config(
                text="Use número ímpar!",
                fg=cor5
            )

            return False

        total_rodadas = valor

        label_config.config(
            text=f"Partida: {total_rodadas} rodadas",
            fg=cor1
        )

        return True

    except ValueError:

        label_config.config(
            text="Digite um número ímpar!",
            fg=cor5
        )

        return False


# =========================================================
# BOTÃO CONFIRMAR RODADAS
# =========================================================

botao_confirmar = tk.Button(
    frame_baixo,
    text="OK",
    font=("Ivy", 9, "bold"),
    bg=cor4,
    fg=cor1,
    relief="flat",
    command=validar_rodadas
)

botao_confirmar.place(
    x=125,
    y=2,
    width=35,
    height=25
)


# =========================================================
# INFORMAÇÃO DA PARTIDA
# =========================================================

label_config = tk.Label(
    frame_baixo,
    text="Partida: 5 rodadas",
    font=("Ivy", 8, "bold"),
    bg=cor0,
    fg=cor1
)

label_config.place(
    x=165,
    y=7
)


# =========================================================
# RODADA ATUAL
# =========================================================

label_rodada = tk.Label(
    frame_baixo,
    text="Rodada 0 / 5",
    font=("Ivy", 10, "bold"),
    bg=cor0,
    fg=cor1
)

label_rodada.place(
    x=75,
    y=32
)


# =========================================================
# ÁREA DAS ESCOLHAS
# =========================================================

# ---------------------------------------------------------
# JOGADOR
# ---------------------------------------------------------

frame_escolha_jogador = Frame(
    frame_baixo,
    bg=cor0
)

frame_escolha_jogador.place(
    x=0,
    y=55,
    width=130,
    height=95
)


# ---------------------------------------------------------
# COMPUTADOR
# ---------------------------------------------------------

frame_escolha_pc = Frame(
    frame_baixo,
    bg=cor0
)

frame_escolha_pc.place(
    x=130,
    y=55,
    width=130,
    height=95
)


# =========================================================
# TÍTULO JOGADOR
# =========================================================

label_jogador_titulo = tk.Label(
    frame_escolha_jogador,
    text="JOGADOR",
    font=("Ivy", 9, "bold"),
    bg=cor0,
    fg=azul_jogador
)

label_jogador_titulo.place(
    x=0,
    y=5,
    width=130
)


# =========================================================
# TÍTULO COMPUTADOR
# =========================================================

label_pc_titulo = tk.Label(
    frame_escolha_pc,
    text="COMPUTADOR",
    font=("Ivy", 9, "bold"),
    bg=cor0,
    fg=roxo_computador
)

label_pc_titulo.place(
    x=0,
    y=5,
    width=130
)


# =========================================================
# ESCOLHA JOGADOR
# =========================================================

label_jogador_escolha = tk.Label(
    frame_escolha_jogador,
    text="?",
    font=("Ivy", 25, "bold"),
    bg=cor0,
    fg=azul_jogador
)

label_jogador_escolha.place(
    x=35,
    y=25,
    width=60,
    height=60
)


# =========================================================
# ESCOLHA COMPUTADOR
# =========================================================

label_pc_escolha = tk.Label(
    frame_escolha_pc,
    text="?",
    font=("Ivy", 25, "bold"),
    bg=cor0,
    fg=roxo_computador
)

label_pc_escolha.place(
    x=35,
    y=25,
    width=60,
    height=60
)


# =========================================================
# LINHA VERTICAL
# =========================================================

linha_vertical = Frame(
    frame_baixo,
    bg=cinza_linha
)

linha_vertical.place(
    x=129,
    y=55,
    width=2,
    height=95
)


# =========================================================
# LINHA HORIZONTAL
# =========================================================

linha_horizontal = Frame(
    frame_baixo,
    bg=cinza_linha
)

linha_horizontal.place(
    x=0,
    y=150,
    width=260,
    height=2
)


# =========================================================
# MOSTRAR ESCOLHA DO COMPUTADOR
# =========================================================

def mostrar_computador(escolha):

    if escolha == "Pedra":

        label_pc_escolha.config(
            image=imagem_pedra,
            text=""
        )

    elif escolha == "Papel":

        label_pc_escolha.config(
            image=imagem_papel,
            text=""
        )

    elif escolha == "Tesoura":

        label_pc_escolha.config(
            image=imagem_tesoura,
            text=""
        )


# =========================================================
# FINALIZAR PARTIDA
# =========================================================

def finalizar_partida():

    # -----------------------------------------------------
    # DESABILITA BOTÕES
    # -----------------------------------------------------

    botao_pedra.config(
        state="disabled"
    )

    botao_papel.config(
        state="disabled"
    )

    botao_tesoura.config(
        state="disabled"
    )

    botao_confirmar.config(
        state="disabled"
    )

    # -----------------------------------------------------
    # DEFINE VENCEDOR
    # -----------------------------------------------------

    if pontos_jogador > pontos_computador:

        texto = "🏆 VOCÊ VENCEU A PARTIDA!"

    elif pontos_computador > pontos_jogador:

        texto = "🤖 COMPUTADOR VENCEU!"

    else:

        texto = "🤝 PARTIDA EMPATADA!"

    label_resultado.config(
        text=texto,
        fg=cor4 if pontos_jogador > pontos_computador else cor5
    )


# =========================================================
# FUNÇÃO SELECIONAR (JOGAR DIRETO)
# =========================================================

def selecionar(escolha):

    global escolha_jogador
    global escolha_computador
    global rodada_atual
    global pontos_jogador
    global pontos_computador
    global pontos_empate

    # Não permite escolher se a partida acabou
    if rodada_atual >= total_rodadas:

        return

    escolha_jogador = escolha

    # -----------------------------------------------------
    # REMOVE DESTAQUE DOS BOTÕES
    # -----------------------------------------------------

    botao_pedra.config(
        relief="flat",
        bd=1
    )

    botao_papel.config(
        relief="flat",
        bd=1
    )

    botao_tesoura.config(
        relief="flat",
        bd=1
    )

    # Destaca a escolha atual
    if escolha == "Pedra":
        botao_pedra.config(relief="solid", bd=3)
        label_jogador_escolha.config(image=imagem_pedra, text="")
    elif escolha == "Papel":
        botao_papel.config(relief="solid", bd=3)
        label_jogador_escolha.config(image=imagem_papel, text="")
    elif escolha == "Tesoura":
        botao_tesoura.config(relief="solid", bd=3)
        label_jogador_escolha.config(image=imagem_tesoura, text="")

    # -----------------------------------------------------
    # NOVA RODADA
    # -----------------------------------------------------

    rodada_atual += 1

    label_rodada.config(
        text=f"Rodada {rodada_atual} / {total_rodadas}"
    )

    # -----------------------------------------------------
    # COMPUTADOR ESCOLHE
    # -----------------------------------------------------

    escolha_computador = random.choice(
        [
            "Pedra",
            "Papel",
            "Tesoura"
        ]
    )

    mostrar_computador(
        escolha_computador
    )

    # -----------------------------------------------------
    # VERIFICA RESULTADO
    # -----------------------------------------------------

    if escolha_jogador == escolha_computador:

        resultado = "EMPATE!"

        pontos_empate += 1

        app_pontos_empate.config(
            text=str(pontos_empate)
        )

    elif (
        (escolha_jogador == "Pedra"
         and escolha_computador == "Tesoura")

        or

        (escolha_jogador == "Papel"
         and escolha_computador == "Pedra")

        or

        (escolha_jogador == "Tesoura"
         and escolha_computador == "Papel")
    ):

        resultado = "VOCÊ VENCEU!"

        pontos_jogador += 1

        app_pontos_pessoa.config(
            text=str(pontos_jogador)
        )

    else:

        resultado = "VOCÊ PERDEU!"

        pontos_computador += 1

        app_pontos_computador.config(
            text=str(pontos_computador)
        )

    # -----------------------------------------------------
    # MOSTRA RESULTADO
    # -----------------------------------------------------

    label_resultado.config(
        text=resultado,
        fg=cor1
    )

    # -----------------------------------------------------
    # VERIFICA SE TERMINOU
    # -----------------------------------------------------

    if rodada_atual >= total_rodadas:

        janela.after(
            500,
            finalizar_partida
        )


# =========================================================
# OPÇÕES
# =========================================================

label_opcoes = tk.Label(
    frame_baixo,
    text="ESCOLHA SUA JOGADA",
    font=("Ivy", 9, "bold"),
    bg=cor0,
    fg=cor1
)

label_opcoes.place(
    x=0,
    y=158,
    width=260
)


# =========================================================
# BOTÃO PEDRA
# =========================================================

botao_pedra = tk.Button(
    frame_baixo,
    image=imagem_pedra,
    width=50,
    height=50,
    bg=cor0,
    activebackground=cor0,
    relief="flat",
    bd=1,
    command=lambda: selecionar("Pedra")
)

botao_pedra.place(
    x=20,
    y=180
)


# =========================================================
# BOTÃO PAPEL
# =========================================================

botao_papel = tk.Button(
    frame_baixo,
    image=imagem_papel,
    width=50,
    height=50,
    bg=cor0,
    activebackground=cor0,
    relief="flat",
    bd=1,
    command=lambda: selecionar("Papel")
)

botao_papel.place(
    x=100,
    y=180
)


# =========================================================
# BOTÃO TESOURA
# =========================================================

botao_tesoura = tk.Button(
    frame_baixo,
    image=imagem_tesoura,
    width=50,
    height=50,
    bg=cor0,
    activebackground=cor0,
    relief="flat",
    bd=1,
    command=lambda: selecionar("Tesoura")
)

botao_tesoura.place(
    x=180,
    y=180
)


# =========================================================
# LINHA
# =========================================================

linha_opcoes = Frame(
    frame_baixo,
    bg=cinza_linha
)

linha_opcoes.place(
    x=0,
    y=240,
    width=260,
    height=1
)


# =========================================================
# RESULTADO
# =========================================================

label_resultado = tk.Label(
    frame_baixo,
    text="Escolha uma opção",
    font=("Ivy", 10, "bold"),
    bg=cor0,
    fg=cor1
)

label_resultado.place(
    x=0,
    y=255,
    width=260,
    height=35
)


# =========================================================
# EMPATES
# =========================================================

frame_empate = Frame(
    frame_baixo,
    width=260,
    height=50,
    bg=cor3
)

frame_empate.place(
    x=0,
    y=305
)


app_empate = tk.Label(
    frame_empate,
    text="EMPATES",
    font=("Ivy", 10, "bold"),
    bg=cor3,
    fg=cor1
)

app_empate.place(
    x=10,
    y=10
)


app_pontos_empate = tk.Label(
    frame_empate,
    text="0",
    font=("Ivy", 20, "bold"),
    bg=cor3,
    fg=cor1
)

app_pontos_empate.place(
    x=100,
    y=5
)


# =========================================================
# NOVA PARTIDA
# =========================================================

def nova_partida():

    global escolha_jogador
    global escolha_computador
    global rodada_atual
    global pontos_jogador
    global pontos_computador
    global pontos_empate

    # -----------------------------------------------------
    # VALIDAR RODADAS
    # -----------------------------------------------------

    if not validar_rodadas():

        return

    # -----------------------------------------------------
    # RESET
    # -----------------------------------------------------

    escolha_jogador = None
    escolha_computador = None

    rodada_atual = 0

    pontos_jogador = 0
    pontos_computador = 0
    pontos_empate = 0

    # -----------------------------------------------------
    # RESET PLACAR
    # -----------------------------------------------------

    app_pontos_pessoa.config(
        text="0"
    )

    app_pontos_computador.config(
        text="0"
    )

    app_pontos_empate.config(
        text="0"
    )

    # -----------------------------------------------------
    # RESET RODADA
    # -----------------------------------------------------

    label_rodada.config(
        text=f"Rodada 0 / {total_rodadas}"
    )

    # -----------------------------------------------------
    # RESET ESCOLHAS
    # -----------------------------------------------------

    label_jogador_escolha.config(
        image="",
        text="?"
    )

    label_pc_escolha.config(
        image="",
        text="?"
    )

    # -----------------------------------------------------
    # RESET BOTÕES
    # -----------------------------------------------------

    botao_pedra.config(
        state="normal",
        relief="flat",
        bd=1
    )

    botao_papel.config(
        state="normal",
        relief="flat",
        bd=1
    )

    botao_tesoura.config(
        state="normal",
        relief="flat",
        bd=1
    )

    botao_confirmar.config(
        state="normal"
    )

    # -----------------------------------------------------
    # RESULTADO
    # -----------------------------------------------------

    label_resultado.config(
        text="Escolha uma opção",
        fg=cor1
    )


# =========================================================
# BOTÃO NOVA PARTIDA
# =========================================================

botao_nova = tk.Button(
    frame_baixo,
    text="NOVA PARTIDA",
    font=("Ivy", 9, "bold"),
    bg=cor2,
    fg=cor1,
    relief="flat",
    command=nova_partida
)

botao_nova.place(
    x=150,
    y=315,
    width=100,
    height=30
)


# =========================================================
# INICIAR
# =========================================================

janela.mainloop()