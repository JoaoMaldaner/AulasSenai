import tkinter as tk
root = tk.Tk()
root.title("Frames aula grid")
#root.geometry("320x600")


for linha in range(3):
    for coluna in range(3):
        tk.Button(root, text=f"Label {linha},{coluna}",
                 relief=tk.RAISED,
                 width=20,
                 height=5).grid(row=linha, column=coluna, padx=5, pady=5)
    tk.Button(root, text="Span 2 columns",
              height=5).grid(row=3, column=0, columnspan=2, sticky="ew", padx=2, pady=2)

    tk.Button(root, text="Span 2 rows",
              width=20, height=10).grid(row=4, column=2, rowspan=2, sticky="ns", padx=2, pady=2)

root.mainloop()
        