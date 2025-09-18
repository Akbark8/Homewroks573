import tkinter as tk
from tkinter import messagebox

MAX_LENGTH = 100

def check_length(event=None):
    text = entry.get()
    if len(text) > MAX_LENGTH:
        messagebox.showwarning("Предупреждение", f"Вы ввели больше {MAX_LENGTH} символов!")
        entry.delete(MAX_LENGTH, tk.END)

root = tk.Tk()
root.title("Ограничение ввода")

label = tk.Label(root, text="Введите текст (до 100 символов):")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

entry.bind("<KeyRelease>", check_length)

root.mainloop()
