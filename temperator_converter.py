import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Temperature Converter")

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        label_result.config(text="Invalid input!")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        label_result.config(text=f"{celsius:.2f} °C")
    except ValueError:
        label_result.config(text="Invalid input!")

# Layout for Celsius to Fahrenheit conversion
label_celsius = tk.Label(root, text="Celsius:")
label_celsius.grid(row=0, column=0, padx=10, pady=10)

entry_celsius = tk.Entry(root)
entry_celsius.grid(row=0, column=1, padx=10, pady=10)

button_convert_to_fahrenheit = tk.Button(root, text="Convert to Fahrenheit", command=celsius_to_fahrenheit)
button_convert_to_fahrenheit.grid(row=0, column=2, padx=10, pady=10)

# Layout for Fahrenheit to Celsius conversion
label_fahrenheit = tk.Label(root, text="Fahrenheit:")
label_fahrenheit.grid(row=1, column=0, padx=10, pady=10)

entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.grid(row=1, column=1, padx=10, pady=10)

button_convert_to_celsius = tk.Button(root, text="Convert to Celsius", command=fahrenheit_to_celsius)
button_convert_to_celsius.grid(row=1, column=2, padx=10, pady=10)

# Label to display the result
label_result = tk.Label(root, text="")
label_result.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Create Quit button
button_quit = tk.Button(root, text="Quit", command=root.quit)
button_quit.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Start the main loop
root.mainloop()
