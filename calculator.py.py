import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))
    entry.config(fg='black')  # Set the text color to black for input numbers

def clear_entry():
    entry.delete(0, tk.END)

def delete_character():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        entry.config(fg='blue')  # Set the text color to blue for the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        entry.config(fg='red')  # Set the text color to red for error messages

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Entry widget to display input and results
entry = tk.Entry(window, width=20, borderwidth=5, fg='black')  # Set the initial text color to black
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Button colors
button_colors = [
    '#008000', '#008000', '#008000', '#008000',
    '#008000', '#008000', '#008000', '#008000',
    '#008000', '#008000', '#008000', '#008000',
    '#008000', '#008000', '#008000', '#008000'
]

# Add buttons to the GUI with colors
row_val = 1
col_val = 0
for button, color in zip(buttons, button_colors):
    tk.Button(window, text=button, padx=20, pady=20, bg=color, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Backspace button
tk.Button(window, text='<-', padx=20, pady=20, bg='#008000', command=delete_character).grid(row=row_val, column=col_val)

# Clear button
tk.Button(window, text='C', padx=20, pady=20, bg='#008000', command=clear_entry).grid(row=row_val, column=col_val + 1)

# Equals button
tk.Button(window, text='=', padx=20, pady=20, bg='#008000', command=calculate_result).grid(row=row_val, column=col_val + 2)

# Run the GUI
window.mainloop()