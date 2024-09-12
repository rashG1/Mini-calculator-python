import tkinter as tk
from math import sqrt

expression = ""
memory = 0

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def sqrtpress():
    try:
        global expression
        result = str(sqrt(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("error")
        expression = ""

def memory_store():
    global memory, expression
    try:
        memory += float(expression)
        equation.set("M+")
        expression = ""
    except:
        equation.set("error")
        expression = ""

def memory_subtract():
    global memory, expression
    try:
        memory -= float(expression)
        equation.set("M-")
        expression = ""
    except:
        equation.set("error")
        expression = ""

def memory_recall():
    global memory
    equation.set(memory)
    expression = str(memory)

def memory_clear():
    global memory
    memory = 0
    equation.set("Memory Cleared")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Advanced Calculator")
    root.geometry("400x600")

    equation = tk.StringVar()

    display = tk.Entry(root, textvariable=equation, font=('arial', 24, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4)
    display.grid(row=0, column=0, columnspan=4)

    button_texts = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ('C', 5, 0), ('sqrt', 5, 1), ('**', 5, 2), ('%', 5, 3),
        ('M+', 6, 0), ('M-', 6, 1), ('MR', 6, 2), ('MC', 6, 3)
    ]

    for (text, row, col) in button_texts:
        if text == '=':
            tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20), bg='lightgreen', command=equalpress).grid(row=row, column=col, ipadx=10, ipady=10)
        elif text == 'C':
            tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20), bg='lightcoral', command=clear).grid(row=row, column=col, ipadx=10, ipady=10)
        elif text == 'sqrt':
            tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20), command=sqrtpress).grid(row=row, column=col, ipadx=10, ipady=10)
        elif text == 'M+':
            tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20), command=memory_store).grid(row=row, column=col, ipadx=10, ipady=10)
        elif text == 'M-':
            tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20), command=memory_subtract).grid(row=row, column=col, ipadx=10, ipady=10)
        elif text == 'MR':
            tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20), command=memory_recall).grid(row=row, column=col, ipadx=10, ipady=10)
        elif text == 'MC':
            tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20), command=memory_clear).grid(row=row, column=col, ipadx=10, ipady=10)
        else:
            tk.Button(root, text=text, padx=20, pady=20, font=('arial', 20), command=lambda t=text: press(t)).grid(row=row, column=col, ipadx=10, ipady=10)

    root.mainloop()
