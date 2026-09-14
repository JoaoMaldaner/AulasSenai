import tkinter as tk
from tkinter import ttk

# dicionario com as cores e seus respectivos valores, multiplicadores e tolerâncias
CORES = {
    "Preto": (0, 1, 20, None), 
    "Marrom": (1, 10, 100, 1),
    "Vermelho": (2, 100, 1000, 2), 
    "Laranja": (3, 1000, 10000, None),
    "Amarelo": (4, 10000, 100000, None), 
    "Verde": (5, 100000, 1000000, 0.5),
    "Azul": (6, 1000000, 10000000, 0.25), 
    "Violeta": (7, 10000000, 100000000, 0.1),
    "Cinza": (8, 100000000, None, 0.05), 
    "Branco": (9, 1000000000, None, None),
    "Dourado": (None, 0.1, None, 5), 
    "Prateado": (None, 0.01, None, 10)
}

# dicionario com as cores e seus respectivos valores em hexadecimal para interface grafica
TK_CORES = {
    "Preto": "#000000", 
    "Marrom": "#8B4513", 
    "Vermelho": "#FF0000",
    "Laranja": "#FFA500", 
    "Amarelo": "#FFFF00", 
    "Verde": "#008000",
    "Azul": "#0000FF", 
    "Violeta": "#8A2BE2", 
    "Cinza": "#808080",
    "Branco": "#FFFFFF", 
    "Dourado": "#FFD700", 
    "Prateado": "#C0C0C0"
}

DIGITOS = list(CORES.keys())[:10] #transforma as cores em uma lista de dígitos (0-9) pega somente os 10 primeiros elementos.
MULTIPLICADORES = list(CORES.keys()) #pega todas as cores como multiplicadors
TOLERANCIAS = ["Marrom", "Vermelho", "Verde", "Azul", "Violeta", "Cinza", "Dourado", "Prateado"] #pega somente as cores com tolerancia

#função para formatar o valor da resistência em ohms, kiloohms ou megaohms
def formatar(valor):
    if valor >= 1_000_000:
        return f"{valor / 1_000_000:g} MΩ"
    if valor >= 1_000:
        return f"{valor / 1_000:g} kΩ"
    return f"{valor:g} Ω"

#função para calcular a resistência com base nas cores selecionadas
def calcular():
    try:
        c1, c2, mult, tol = v1.get(), v2.get(), vm.get(), vt.get() #variaveis que recebem os valores selecionados nos comboboxes
        d1, d2 = CORES[c1][0], CORES[c2][0] #digitos correspondentes às cores selecionadas [0] é o dígito da cor e a primeira posição do dicionario
        fator = CORES[mult][1] #fator de multiplicação correspondente à cor selecionada [1] é o fator de multiplicação da cor e a segunda posição do dicionario
        resistencia = (d1 * 10 + d2) * fator

        tolerancia = CORES[tol][3] #tolerancia = CORES[tol][3] #tolerancia correspondente à cor selecionada [3]
        resultado.config(text=f"{formatar(resistencia)} ± {tolerancia}%")
        desenhar([c1, c2, mult, tol])
    except:
        resultado.config(text="Selecione todas as cores")

#função para as cores correspondentes ao valor da resistência digitado
def valor_para_cores():
    try:
        valor = float(entrada_valor.get())
        unidade = unidade_var.get()
        fator_unidade = {"Ω": 1, "kΩ": 1_000, "MΩ": 1_000_000}[unidade]
        valor *= fator_unidade

        if valor <= 0:
            raise ValueError

        encontrado = None

        for mult, dados in CORES.items():
            fator = dados[1]
            if fator and valor / fator >= 10 and valor / fator <= 99: #testa se o valor dividido tem dois digitos entre 10 e 99
                numero = valor / fator #atribui o valor dividido a variavel
                if numero.is_integer(): #valida se é um inteiro
                    numero = int(numero)
                    d1, d2 = numero // 10, numero % 10
                    encontrado = [DIGITOS[d1], DIGITOS[d2], mult] #atribui os digitos a variavel encontrado.
                    break

        if not encontrado:
            resultado.config(text="Valor não representável") #se o valor não for represntavel retorna o erro
        
            return

        tolerancia = vt.get() #pega a tolerancia selecionada no combobox
        resultado.config(text=f"{formatar(valor)} ± {CORES[tolerancia][3]}%") #exibe o valor formatado com a tolerância
        v1.set(encontrado[0])
        v2.set(encontrado[1])
        vm.set(encontrado[2])
        desenhar(encontrado + [tolerancia]) #chama a função desenhar passando as cores encontradas e a tolerancia selecionada

    except:
        resultado.config(text="Digite um valor válido")


def desenhar(cores):
    canvas.delete("all")

    # criar os fios do resistor
    canvas.create_line(30, 100, 120, 100, width=4)
    canvas.create_line(380, 100, 470, 100, width=4)

    # Corpo
    canvas.create_rectangle(120, 65, 380, 135, fill="#D2B48C", outline="black", width=2)

    # criar as faixas de cores dos resistores
    posicoes = [160, 210, 260, 330]
    larguras = [20, 20, 20, 15]

    for cor, x, largura in zip(cores, posicoes, larguras):
        canvas.create_rectangle(
            x, 65, x + largura, 135,
            fill=TK_CORES[cor],
            outline="black"
        )

        # nome da cor abaixo da faixa
        canvas.create_text(
            x + largura / 2,
            155,
            text=cor,
            font=("Arial", 9, "bold")
        )

# Janela - montando a interface gráfica
janela = tk.Tk()
janela.title("Calculadora de Resistores")
janela.geometry("800x920")
janela.resizable(False, False)#não permite redimensionar a janela

tk.Label(
    janela, text="CALCULADORA DE RESISTORES",
    font=("Arial", 18, "bold")
).pack(pady=15)

# setar as cores
frame_cores = tk.LabelFrame(janela, text="Código de Cores", padx=10, pady=10)
frame_cores.pack(padx=20, fill="x")

#deixei setado o valor inicial do resistor como 1kΩ ± 5% (Marrom, Preto, Vermelho, Dourado)
v1 = tk.StringVar(value="Marrom")#variaveis que armazenam os valores selecionados nos comboboxes
v2 = tk.StringVar(value="Preto")
vm = tk.StringVar(value="Vermelho")
vt = tk.StringVar(value="Dourado")

#definição da função combo para criar os comboboxes de seleção de cores
def combo(frame, texto, variavel, valores, linha):
    tk.Label(frame, text=texto).grid(row=linha, column=0, sticky="w", pady=5)
    ttk.Combobox(
        frame, textvariable=variavel,
        values=valores, state="readonly", width=18
    ).grid(row=linha, column=1, padx=10)

combo(frame_cores, "1ª faixa:", v1, DIGITOS, 0) #aplica cada combo em uma linha 
combo(frame_cores, "2ª faixa:", v2, DIGITOS, 1)
combo(frame_cores, "Multiplicador:", vm, MULTIPLICADORES, 2)
combo(frame_cores, "Tolerância:", vt, TOLERANCIAS, 3)
#botão para calcular a resistência com base nas cores selecionadas
tk.Button(
    frame_cores, text="CALCULAR",
    command=calcular, width=20
).grid(row=4, column=0, columnspan=2, pady=10)

# atribuindo valor das cores
frame_valor = tk.LabelFrame(janela, text="Valor → Código de Cores", padx=10, pady=10)
frame_valor.pack(padx=20, pady=10, fill="x")

entrada_valor = tk.Entry(frame_valor, width=15)
entrada_valor.grid(row=0, column=0, padx=5)

unidade_var = tk.StringVar(value="Ω")
ttk.Combobox(
    frame_valor, textvariable=unidade_var,
    values=["Ω", "kΩ", "MΩ"], state="readonly", width=6
).grid(row=0, column=1)

tk.Button(
    frame_valor, text="CONVERTER",
    command=valor_para_cores
).grid(row=0, column=2, padx=10)

# Bonus: Calculadora de resistor para LED
frame_led = tk.LabelFrame(
    janela, text="Calcular Resistor para LED (Lei de Ohm)",
    padx=10, pady=10
)
frame_led.pack(padx=20, pady=10, fill="x")

tk.Label(frame_led, text="Tensão da fonte (V):").grid(row=0, column=0, sticky="w", pady=4)
entrada_fonte = tk.Entry(frame_led, width=10)
entrada_fonte.grid(row=0, column=1, padx=5)

tk.Label(frame_led, text="Tensão do LED (V):").grid(row=1, column=0, sticky="w", pady=4)
entrada_led = tk.Entry(frame_led, width=10)
entrada_led.grid(row=1, column=1, padx=5)

tk.Label(frame_led, text="Corrente (mA):").grid(row=2, column=0, sticky="w", pady=4)
entrada_corrente = tk.Entry(frame_led, width=10)
entrada_corrente.grid(row=2, column=1, padx=5)

resultado_led = tk.Label(
    frame_led, text="Resistor: ---",
    font=("Arial", 14, "bold")
)
resultado_led.grid(row=4, column=0, columnspan=3, pady=8)


def calcular_led():
    try:
        fonte = float(entrada_fonte.get())
        led = float(entrada_led.get())
        corrente_ma = float(entrada_corrente.get())

        if fonte <= led or corrente_ma <= 0:
            resultado_led.config(text="Verifique os valores informados")
            return

        corrente = corrente_ma / 1000
        resistencia = (fonte - led) / corrente

        # valores comerciais, chama os valores mais proximo dos resistores comercializados
        valores = [
            10, 12, 15, 18, 22, 27, 33, 39,
            47, 51, 56, 62, 68, 75, 82, 91
        ]

        escala = 1

        while resistencia / escala >= 100:
            escala *= 10 #multiplica a escala por 10 enquanto a resistência dividida pela escala for maior ou igual a 100

        while resistencia / escala < 10:
            escala /= 10 #divide a escala por 10 enquanto a resistência dividida pela escala for menor que 10

        base = resistencia / escala #cria a variavel base que recebe a resistencia dividida pela escala

        #encontra o valor comercial mais próximo
        comercial = min( 
            valores,
            key=lambda x: abs(x - base)
        ) * escala

        resultado_led.config(
            text=f"Resistor: {resistencia:g} Ω\n"
                 f"Valor comercial aproximado: {comercial:g} Ω"
        )

        # envia o valor comercial para a calculadora de cores
        # usando somente o valor Ohms para facilitar a conversão.
        entrada_valor.delete(0, tk.END)  
        entrada_valor.insert(0, str(comercial))
        unidade_var.set("Ω")

        # converte automaticamente para as cores
        valor_para_cores()

    except ValueError:
        resultado_led.config(
            text="Digite apenas valores numéricos"
        )


tk.Button(
    frame_led,
    text="CALCULAR RESISTOR",
    command=calcular_led,
    width=22
).grid(row=3, column=0, columnspan=3, pady=8)

# apresntando resultado
resultado = tk.Label(
    janela, text="1 kΩ ± 5%",
    font=("Arial", 20, "bold")
)
resultado.pack(pady=15)

# chamando canvas
canvas = tk.Canvas(
    janela, width=500, height=180,
    bg="white", highlightthickness=1
)
canvas.pack()

desenhar(["Marrom", "Preto", "Vermelho", "Dourado"])

janela.mainloop()