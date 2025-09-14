import tkinter as tk
import random

root = tk.Tk()
root.title("Случайное имя")

names = ["Алексей", "Мария", "Иван", "Ольга", "Елена", "Дмитрий"]

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

def set_random_name():
    entry.delete(0, tk.END)
    entry.insert(0, random.choice(names))

btn = tk.Button(root, text="Случайное имя", command=set_random_name)
btn.pack(pady=5)

root.mainloop()
