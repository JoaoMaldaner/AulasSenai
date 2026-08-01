import tkinter as tk
root = tk.Tk()
root.title("Frames aula 31-7")
root.config(bg="#0C2FA1")

frame = tk.Frame(root, width=420, height=220)
frame.pack(padx=10, pady=10)

a_frame = tk.Frame(frame, width=190, height=190, bg= "#FF0000")
a_frame.pack(side= "top", padx=10, pady=10)

b_frame = tk.Frame(frame, width=190, height=190, bg= "green")
b_frame.pack(side= "bottom", padx=10, pady=10)

root.mainloop()