import tkinter as tk
root = tk.Tk()
root.title("Frames aula 31-7")
root.geometry("340x200")
#root.config(bg="#0C2FA1")

tk.Button(root, text="top button!").pack()
tk.Label(root, text="Hello, Left").pack(side="left")
tk.Label(root, text="Hello, Right").pack(side="right")
tk.Checkbutton(root, text="Uma opção na parte inferior").pack(side=tk.BOTTOM)


root.mainloop()