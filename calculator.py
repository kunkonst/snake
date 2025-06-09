import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Variable to store current calculation
        self.current = ""
        
        # Create display
        self.display_var = tk.StringVar()
        self.display = ttk.Entry(
            root, 
            textvariable=self.display_var, 
            justify="right",
            font=('Arial', 20),
            state='readonly'
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create and place buttons
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(
                root, 
                text=button,
                command=cmd
            ).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        ttk.Button(
            root, 
            text='C',
            command=self.clear
        ).grid(row=row, column=col, columnspan=4, padx=2, pady=2, sticky="nsew")

        # Configure grid weights
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def click(self, button):
        if button == '=':
            try:
                result = eval(self.current)
                self.display_var.set(result)
                self.current = str(result)
            except:
                messagebox.showerror("Error", "Invalid Expression")
                self.clear()
        else:
            self.current += button
            self.display_var.set(self.current)

    def clear(self):
        self.current = ""
        self.display_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop() 