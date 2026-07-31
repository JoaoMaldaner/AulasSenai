import tkinter as tk

root = tk.Tk()
root.geometry("300x250")
root.title("Calculadora de IMC")

tk.Label(root, text="Peso (kg):").pack()

entry_peso = tk.Entry(root)
entry_peso.pack()

tk.Label(root, text="Altura (m):").pack()

entry_altura = tk.Entry(root)
entry_altura.pack()

resultado = tk.Label(root, text="")
resultado.pack(pady=10)

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Magreza"
            mensagem = "Você está abaixo do peso ideal."
        elif imc < 25:
            classificacao = "Peso saudável"
            mensagem = "Parabéns! Seu peso está dentro da faixa saudável."
        elif imc < 30:
            classificacao = "Sobrepeso"
            mensagem = "É recomendado adotar hábitos mais saudáveis."
        elif imc < 35:
            classificacao = "Obesidade Grau I"
            mensagem = "Procure orientação médica e pratique atividades físicas."
        elif imc < 40:
            classificacao = "Obesidade Grau II"
            mensagem = "É importante buscar acompanhamento médico."
        else:
            classificacao = "Obesidade Grau III"
            mensagem = "Procure atendimento médico para avaliação e tratamento."

        resultado.config(
            text=f"IMC: {imc:.2f}\n"
                 f"Classificação: {classificacao}\n\n"
                 f"{mensagem}"
        )

    except ValueError:
        resultado.config(text="Digite valores válidos!")

    

botao = tk.Button(root, text="Calcular IMC", command=calcular_imc)
botao.pack(pady=10)



root.mainloop()