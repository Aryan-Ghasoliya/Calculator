import tkinter as tk

def button_click(value):
    """Handle button clicks."""
    if value == "=":
        try:
            result = eval(entry.get())  # Evaluate the expression in the entry widget
            entry.delete(0, tk.END)    # Clear the entry widget
            entry.insert(tk.END, str(result))  # Display the result
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)  # Clear the entry widget
    else:
        entry.insert(tk.END, value)  # Append the button value to the entry widget

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget for displaying the expression/result
entry = tk.Entry(root, width=20, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create and place the buttons on the grid
row, col = 1, 0
for button in buttons:
    tk.Button(
        root, text=button, width=5, height=2, font=("Arial", 14),
        command=lambda value=button: button_click(value)
    ).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()
