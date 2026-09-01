import tkinter as tk
from tkinter import ttk, messagebox

# CÓDIGO DE CORES

CORES = {
    "Preto": {
        "valor": 0,
        "hex": "#000000"
    },
    "Marrom": {
        "valor": 1,
        "hex": "#8B4513"
    },
    "Vermelho": {
        "valor": 2,
        "hex": "#FF0000"
    },
    "Laranja": {
        "valor": 3,
        "hex": "#FF8C00"
    },
    "Amarelo": {
        "valor": 4,
        "hex": "#FFFF00"
    },
    "Verde": {
        "valor": 5,
        "hex": "#008000"
    },
    "Azul": {
        "valor": 6,
        "hex": "#0000FF"
    },
    "Violeta": {
        "valor": 7,
        "hex": "#8A2BE2"
    },
    "Cinza": {
        "valor": 8,
        "hex": "#808080"
    },
    "Branco": {
        "valor": 9,
        "hex": "#FFFFFF"
    }
}

MULTIPLICADORES = {
    "Preto": 1,
    "Marrom": 10,
    "Vermelho": 100,
    "Laranja": 1_000,
    "Amarelo": 10_000,
    "Verde": 100_000,
    "Azul": 1_000_000,
    "Violeta": 10_000_000,
    "Cinza": 100_000_000,
    "Branco": 1_000_000_000,
}

TOLERANCIAS = {
    "Marrom": 1,
    "Vermelho": 2,
    "Verde": 0.5,
    "Azul": 0.25,
    "Violeta": 0.1,
    "Cinza": 0.05,
    "Dourado": 5,
    "Prateado": 10
}

# FUNÇÕES

def formatar_resistencia(valor):
    """Converte Ohms para Ohm, kOhm ou MOhm."""

    if valor >= 1_000_000:
        return f"{valor / 1_000_000:g} MΩ"

    elif valor >= 1_000:
        return f"{valor / 1_000:g} kΩ"

    else:
        return f"{valor:g} Ω"


def obter_resistencia():

    try:

        cor1 = combo_cor1.get()
        cor2 = combo_cor2.get()
        cor3 = combo_cor3.get()
        tolerancia = combo_tolerancia.get()

        if not cor1 or not cor2 or not cor3 or not tolerancia:
            messagebox.showwarning(
                "Atenção",
                "Selecione todas as cores."
            )
            return

        # Primeiros dois algarismos
        primeiro = CORES[cor1]["valor"]
        segundo = CORES[cor2]["valor"]

        numero = primeiro * 10 + segundo

        # Multiplicador
        multiplicador = MULTIPLICADORES[cor3]

        resistencia = numero * multiplicador

        # Tolerância
        tol = TOLERANCIAS[tolerancia]

        erro = resistencia * tol / 100

        minimo = resistencia - erro
        maximo = resistencia + erro

        resultado = (
            f"Resistência: {formatar_resistencia(resistencia)}\n\n"
            f"Tolerância: ±{tol}%\n\n"
            f"Mínimo: {formatar_resistencia(minimo)}\n"
            f"Máximo: {formatar_resistencia(maximo)}"
        )

        label_resultado.config(text=resultado)

        desenhar_resistor(
            [cor1, cor2, cor3, tolerancia]
        )

    except Exception as erro:

        messagebox.showerror(
            "Erro",
            str(erro)
        )


def desenhar_resistor(cores):

    canvas.delete("all")

    # Fios
    canvas.create_line(
        30, 100,
        130, 100,
        width=4
    )

    canvas.create_line(
        370, 100,
        470, 100,
        width=4
    )

    # Corpo do resistor
    canvas.create_rectangle(
        130, 60,
        370, 140,
        fill="#E6C78B",
        outline="black",
        width=2
    )

    # Posições das faixas
    posicoes = [
        160,
        205,
        250,
        310
    ]

    larguras = [
        25,
        25,
        25,
        20
    ]

    for cor, x, largura in zip(
        cores,
        posicoes,
        larguras
    ):

        hex_cor = CORES[cor]["hex"] if cor in CORES else (
            "#D4AF37" if cor == "Dourado" else "#C0C0C0"
        )

        canvas.create_rectangle(
            x,
            60,
            x + largura,
            140,
            fill=hex_cor,
            outline="black"
        )


def resistencia_para_cores():

    try:

        valor = float(entry_resistencia.get())

        unidade = combo_unidade.get()

        if unidade == "Ω":
            resistencia = valor

        elif unidade == "kΩ":
            resistencia = valor * 1_000

        elif unidade == "MΩ":
            resistencia = valor * 1_000_000

        else:
            return

        if resistencia <= 0:
            raise ValueError(
                "Informe uma resistência maior que zero."
            )

        # Procurar combinação de duas casas
        # + multiplicador
        encontrada = False

        for cor1, dados1 in CORES.items():

            if dados1["valor"] == 0:
                continue

            for cor2, dados2 in CORES.items():

                numero = (
                    dados1["valor"] * 10
                    + dados2["valor"]
                )

                for cor3, multiplicador in MULTIPLICADORES.items():

                    calculada = numero * multiplicador

                    if calculada == resistencia:

                        combo_cor1.set(cor1)
                        combo_cor2.set(cor2)
                        combo_cor3.set(cor3)

                        # Mantém tolerância em 5%
                        combo_tolerancia.set("Dourado")

                        obter_resistencia()

                        encontrada = True
                        break

                if encontrada:
                    break

            if encontrada:
                break

        if not encontrada:

            messagebox.showinfo(
                "Resultado",
                "Esse valor não pode ser representado "
                "exatamente usando 3 faixas."
            )

    except ValueError:

        messagebox.showerror(
            "Erro",
            "Digite um valor numérico válido."
        )


def calcular_led():

    try:

        tensao = float(entry_tensao.get())
        led = float(entry_led.get())
        corrente = float(entry_corrente.get())

        # Corrente informada em mA
        corrente_ampere = corrente / 1000

        if tensao <= led:
            messagebox.showwarning(
                "Atenção",
                "A tensão da fonte deve ser maior "
                "que a tensão do LED."
            )
            return

        if corrente_ampere <= 0:
            raise ValueError(
                "A corrente deve ser maior que zero."
            )

        # Tensão sobre o resistor
        tensao_resistor = tensao - led

        # Lei de Ohm
        resistencia = (
            tensao_resistor /
            corrente_ampere
        )

        resultado_led = (
            f"Tensão da fonte: {tensao:g} V\n"
            f"Tensão do LED: {led:g} V\n"
            f"Corrente: {corrente:g} mA\n\n"
            f"Tensão no resistor: "
            f"{tensao_resistor:g} V\n\n"
            f"Resistência calculada:\n"
            f"{formatar_resistencia(resistencia)}"
        )

        label_resultado_led.config(
            text=resultado_led
        )

    except ValueError:

        messagebox.showerror(
            "Erro",
            "Preencha todos os campos corretamente."
        )

# JANELA


janela = tk.Tk()

janela.title(
    "Calculadora de Resistores"
)

janela.geometry(
    "850x700"
)

janela.resizable(
    False,
    False
)

# TÍTULO

titulo = tk.Label(
    janela,
    text="CALCULADORA DE RESISTORES",
    font=("Arial", 20, "bold")
)

titulo.pack(
    pady=15
)

# FRAME CÓDIGO DE CORES

frame_cores = ttk.LabelFrame(
    janela,
    text="Código de Cores"
)

frame_cores.pack(
    padx=20,
    pady=10,
    fill="x"
)


# Cor 1
ttk.Label(
    frame_cores,
    text="1ª Faixa:"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

combo_cor1 = ttk.Combobox(
    frame_cores,
    values=list(CORES.keys()),
    state="readonly",
    width=15
)

combo_cor1.grid(
    row=0,
    column=1
)

combo_cor1.set("Marrom")


# Cor 2
ttk.Label(
    frame_cores,
    text="2ª Faixa:"
).grid(
    row=0,
    column=2,
    padx=10
)

combo_cor2 = ttk.Combobox(
    frame_cores,
    values=list(CORES.keys()),
    state="readonly",
    width=15
)

combo_cor2.grid(
    row=0,
    column=3
)

combo_cor2.set("Preto")


# Cor 3
ttk.Label(
    frame_cores,
    text="Multiplicador:"
).grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

combo_cor3 = ttk.Combobox(
    frame_cores,
    values=list(CORES.keys()),
    state="readonly",
    width=15
)

combo_cor3.grid(
    row=1,
    column=1
)

combo_cor3.set("Vermelho")


# Tolerância
ttk.Label(
    frame_cores,
    text="Tolerância:"
).grid(
    row=1,
    column=2,
    padx=10
)

combo_tolerancia = ttk.Combobox(
    frame_cores,
    values=list(TOLERANCIAS.keys()),
    state="readonly",
    width=15
)

combo_tolerancia.grid(
    row=1,
    column=3
)

combo_tolerancia.set("Dourado")


# Botão calcular
botao_calcular = ttk.Button(
    frame_cores,
    text="CALCULAR RESISTOR",
    command=obter_resistencia
)

botao_calcular.grid(
    row=2,
    column=0,
    columnspan=4,
    pady=15
)


# Resultado
label_resultado = tk.Label(
    frame_cores,
    text="Selecione as cores",
    font=("Arial", 11),
    justify="left"
)

label_resultado.grid(
    row=3,
    column=0,
    columnspan=4,
    pady=10
)

# RESISTÊNCIA -> CORES

frame_valor = ttk.LabelFrame(
    janela,
    text="Informar valor do resistor"
)

frame_valor.pack(
    padx=20,
    pady=10,
    fill="x"
)

entry_resistencia = ttk.Entry(
    frame_valor,
    width=15
)

entry_resistencia.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

combo_unidade = ttk.Combobox(
    frame_valor,
    values=["Ω", "kΩ", "MΩ"],
    state="readonly",
    width=8
)

combo_unidade.grid(
    row=0,
    column=1
)

combo_unidade.set("Ω")

botao_converter = ttk.Button(
    frame_valor,
    text="VALOR → CORES",
    command=resistencia_para_cores
)

botao_converter.grid(
    row=0,
    column=2,
    padx=15
)

# CANVAS
frame_canvas = ttk.LabelFrame(
    janela,
    text="Visualização do Resistor"
)

frame_canvas.pack(
    padx=20,
    pady=10
)

canvas = tk.Canvas(
    frame_canvas,
    width=500,
    height=200,
    bg="white"
)

canvas.pack(
    padx=10,
    pady=10
)

desenhar_resistor(
    ["Marrom", "Preto", "Vermelho", "Dourado"]
)



# CALCULADORA LED
frame_led = ttk.LabelFrame(
    janela,
    text="Calcular resistor para LED - Lei de Ohm"
)

frame_led.pack(
    padx=20,
    pady=10,
    fill="x"
)


ttk.Label(
    frame_led,
    text="Fonte (V):"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=8
)

entry_tensao = ttk.Entry(
    frame_led,
    width=10
)

entry_tensao.grid(
    row=0,
    column=1
)


ttk.Label(
    frame_led,
    text="LED (V):"
).grid(
    row=0,
    column=2,
    padx=5
)

entry_led = ttk.Entry(
    frame_led,
    width=10
)

entry_led.grid(
    row=0,
    column=3
)


ttk.Label(
    frame_led,
    text="Corrente (mA):"
).grid(
    row=0,
    column=4,
    padx=5
)

entry_corrente = ttk.Entry(
    frame_led,
    width=10
)

entry_corrente.grid(
    row=0,
    column=5
)


botao_led = ttk.Button(
    frame_led,
    text="CALCULAR",
    command=calcular_led
)

botao_led.grid(
    row=1,
    column=0,
    columnspan=6,
    pady=10
)


label_resultado_led = tk.Label(
    frame_led,
    text="Informe os valores do projeto.",
    font=("Arial", 10),
    justify="left"
)

label_resultado_led.grid(
    row=2,
    column=0,
    columnspan=6,
    pady=5
)


# ============================================================
# INICIAR
# ============================================================

janela.mainloop()

