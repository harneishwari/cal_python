import tkinter as tk

#function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

#  the main application window
root = tk.Tk()
root.title("Calculator")

# entry widget for user input
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

#  buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# button for clearing the enter operation
tk.Button(root, text='C', width=5, command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val)

#  button for calculating the result
tk.Button(root, text='=', width=5, command=calculate).grid(row=row_val, column=col_val + 1)


root.mainloop()
