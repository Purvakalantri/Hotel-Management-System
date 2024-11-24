import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Basic Calculator")

# Entry widget to display the input and result
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to update the entry field when buttons are pressed
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the entry field
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate and display the result
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle the basic operations
def button_operation(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + operator)

# Define the button layout and their respective commands
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create number, operator, and equal buttons
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=40, pady=20, command=button_equal)
    elif text in ('+', '-', '*', '/'):
        button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_operation(t))
    else:
        button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Create Clear button
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_clear.grid(row=5, column=0, columnspan=2)

# Create Quit button
button_quit = tk.Button(root, text="Quit", padx=79, pady=20, command=root.quit)
button_quit.grid(row=5, column=2, columnspan=2)

# Start the main loop
root.mainloop()
