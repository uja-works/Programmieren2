import tkinter as tk
import math

def click(event):
    global entry_text
    text = event.widget.cget("text")
    if text == "=":
        try:
            # Evaluieren des Ausdrucks mit math-Funktionen
            expression = entry_text.get()
            # Ersetzung der trigonometrischen Funktionen durch math-Funktionen
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            expression = expression.replace("pi", "math.pi")
            expression = expression.replace("e", "math.e")
            result = eval(expression)
            entry_text.set(result)
        except Exception as e:
            entry_text.set("Error")
    elif text == "C":
        entry_text.set("")  # Löscht den aktuellen Ausdruck
    else:
        entry_text.set(entry_text.get() + text)  # Fügt die Taste zur Eingabe hinzu

# Hauptfenster erstellen
root = tk.Tk()
root.title("Taschenrechner")

# Eingabefeld erstellen
entry_text = tk.StringVar()
entry = tk.Entry(root, textvar=entry_text, font=("Arial", 20), bd=8, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Buttons erstellen
buttons = [
    "sin", "cos", "tan", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "C", "0", ".", "=",
    "pi", "e", "(", ")"
]

row = 1
col = 0
for button in buttons:
    btn = tk.Button(root, text=button, font=("Arial", 18), width=5, height=2, relief=tk.RAISED)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Dynamisches Grid
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(row + 1):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()