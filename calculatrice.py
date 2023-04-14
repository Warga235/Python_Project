import tkinter as tk
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # création des widgets de l'interface graphique
        self.entry = tk.Entry(
            master, width=30, borderwidth=5, font=('Arial', 12))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        button_list = [
            'C', 'AC', 'sin', 'cos',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # création des boutons de l'interface graphique
        for i, button in enumerate(button_list):
            row = i // 4 + 1
            col = i % 4
            self.create_button(button, row, col)

    def create_button(self, label, row, col):
        if label == 'C':
            cmd = self.clear_entry
        elif label == 'AC':
            cmd = self.clear_all
        elif label == '=':
            cmd = self.calculate
        else:
            def cmd(x=label): return self.add_to_entry(x)

        button = tk.Button(self.master, text=label,
                           width=5, height=2, command=cmd)
        button.grid(row=row, column=col, padx=5, pady=5)

    def add_to_entry(self, char):
        self.entry.insert(tk.END, char)

    def clear_entry(self):
        self.entry.delete(len(self.entry.get())-1, tk.END)

    def clear_all(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            expr = self.entry.get()
            result = eval(expr)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
