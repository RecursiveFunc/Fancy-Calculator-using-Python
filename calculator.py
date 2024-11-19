import tkinter as tk
from tkinter import messagebox
import math
import locale

# Set locale for number formatting
locale.setlocale(locale.LC_ALL, "")  # Use the default system locale


# Function to format numbers with commas and decimals
def format_number(number):
    try:
        return locale.format_string("%g", float(number), grouping=True)
    except ValueError:
        return number


# Function to handle button clicks
def button_click(number):
    entry.insert(tk.END, str(number))


# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)


# Function to perform the calculation
def calculate():
    try:
        result = eval(entry.get().replace(",", ""))
        entry.delete(0, tk.END)
        entry.insert(0, format_number(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed!")
    except Exception:
        messagebox.showerror("Error", "Invalid input!")


# Function to calculate percentage
def calculate_percentage():
    try:
        current = float(entry.get().replace(",", ""))
        result = current / 100
        entry.delete(0, tk.END)
        entry.insert(0, format_number(result))
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")


# Function to calculate square root
def calculate_sqrt():
    try:
        current = float(entry.get().replace(",", ""))
        if current < 0:
            raise ValueError("Negative number")
        result = math.sqrt(current)
        entry.delete(0, tk.END)
        entry.insert(0, format_number(result))
    except ValueError:
        messagebox.showerror("Error", "Enter a non-negative number")


# Function to create buttons with hover effects
def create_button(text, row, col, command, style):
    button = tk.Button(window, text=text, command=command, **style)
    button.bind("<Enter>", lambda e: e.widget.config(bg="#81c784"))
    button.bind("<Leave>", lambda e: e.widget.config(bg=style["bg"]))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)


# Create the main window
window = tk.Tk()
window.title("Efficient Calculator")
window.configure(bg="#f0f0f0")  # Set background color

# Allow resizing
window.rowconfigure(0, weight=1)  # Entry field row
for i in range(1, 6):  # Button rows
    window.rowconfigure(i, weight=1)
for i in range(4):  # Columns
    window.columnconfigure(i, weight=1)

# Entry field for input and output
entry = tk.Entry(
    window, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Custom button styles
button_style = {
    "font": ("Arial", 14, "bold"),
    "fg": "#ffffff",
    "bg": "#4caf50",
    "activebackground": "#388e3c",
    "activeforeground": "#ffffff",
    "relief": "raised",
    "bd": 3,
}

# Button configurations
button_config = [
    ("7", 1, 0, lambda: button_click("7")),
    ("8", 1, 1, lambda: button_click("8")),
    ("9", 1, 2, lambda: button_click("9")),
    ("/", 1, 3, lambda: button_click("/")),
    ("4", 2, 0, lambda: button_click("4")),
    ("5", 2, 1, lambda: button_click("5")),
    ("6", 2, 2, lambda: button_click("6")),
    ("*", 2, 3, lambda: button_click("*")),
    ("1", 3, 0, lambda: button_click("1")),
    ("2", 3, 1, lambda: button_click("2")),
    ("3", 3, 2, lambda: button_click("3")),
    ("-", 3, 3, lambda: button_click("-")),
    ("C", 4, 0, clear),
    ("0", 4, 1, lambda: button_click("0")),
    ("=", 4, 2, calculate),
    ("+", 4, 3, lambda: button_click("+")),
    ("%", 5, 0, calculate_percentage),
    ("√", 5, 1, calculate_sqrt),
]

# Create buttons dynamically
for text, row, col, command in button_config:
    style = button_style.copy()
    if text == "C":
        style.update(bg="#f44336", activebackground="#d32f2f")
    elif text == "=":
        style.update(bg="#ff9800", activebackground="#f57c00")
    elif text == "%":
        style.update(bg="#2196f3", activebackground="#1976d2")
    elif text == "√":
        style.update(bg="#673ab7", activebackground="#512da8")
    create_button(text, row, col, command, style)

# Run the application
window.mainloop()
