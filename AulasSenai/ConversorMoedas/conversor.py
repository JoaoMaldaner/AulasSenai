import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
root.title("Frames aula grid")
#root.geometry("620x600")


taxas = {
    "USD": 1.00,
    "EUR": 0.92,
    "BRL": 5.50,
    "GPB": 0.79,
    "JPY": 157.00
}


def converter():

    try:
        valor = float(entry_valor.get())
        moeda_origem = moedaOrigem.get()
        moeda_destino = moedaDestino.get()

        #converter USD

        valor_usd = valor / taxas[moeda_origem]
        valor_convertido = valor_usd * taxas[moeda_destino]

        #converter para EUR

        valor_eur = valor / taxas[moeda_origem]
        valor_convertido = valor_eur * taxas[moeda_destino]

        #converter para BRL

        valor_brl = valor / taxas[moeda_origem]
        valor_convertido = valor_brl * taxas[moeda_destino]

        #converter para GPB

        valor_gpb = valor / taxas[moeda_origem]
        valor_convertido = valor_gpb * taxas[moeda_destino]

        #converter para JPY

        valor_jpy = valor / taxas[moeda_origem]
        valor_convertido = valor_jpy * taxas[moeda_destino]

        #tk.messagebox.showinfo("Resultado", f"{valor} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}")

        lbl_resultado.config(text=f"{valor} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}")

    except ValueError:
        tk.messagebox.showerror("Erro", "Valor inválido. Digite um número válido.")





tk.Label(root, text="Valor:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_valor = tk.Entry(root)
entry_valor.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

tk.Label(root, text="Moeda de Origem:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
moedaOrigem = ttk.Combobox(root,values=list(taxas.keys()), state="readonly")
moedaOrigem.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

tk.Label(root, text="Moeda de Destino:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
moedaDestino = ttk.Combobox(root,values=list(taxas.keys()), state="readonly")
moedaDestino.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

tk.Button(root, text="Converter", command=converter).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

lbl_resultado = tk.Label(root, text="")
lbl_resultado.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()