import tkinter as tk

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + value)

def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget for displaying the result
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0
for button in buttons:
    btn = tk.Button(window, text=button, width=5, command=lambda value=button: button_click(value))
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the clear button
clear_btn = tk.Button(window, text="C", width=5, command=clear)
clear_btn.grid(row=row, column=col)

# Run the main loop
window.mainloop()
