import tkinter as tk
root = tk.Tk()
root.title("Frames aula 31-7")
root.config(bg="#0C2FA1")

frame = tk.Frame(root, width=200, height=200)
frame.pack(padx=10, pady=10)

nested_frame = tk.Frame(frame, width=190, height=190, bg= "#FF0000")
nested_frame.pack(padx=10, pady=10)

root.mainloop()