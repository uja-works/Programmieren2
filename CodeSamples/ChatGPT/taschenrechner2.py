import tkinter as tk

def click(event):
    global entry_text
    text = event.widget.cget("text")
    if text == "=":
        try:
            # Evaluiert den eingegebenen Ausdruck und gibt das Ergebnis aus
            result = eval(entry_text.get())
            entry_text.set(result)
        except Exception:
            entry_text.set("Error")
    elif text == "C":
        entry_text.set("")  # Löscht den Inhalt des Eingabefeldes
    else:
        entry_text.set(entry_text.get() + text)  # Fügt die Taste zum Ausdruck hinzu

# Hauptfenster erstellen
root = tk.Tk()
root.title("Taschenrechner")

# Eingabefeld erstellen
entry_text = tk.StringVar()
entry = tk.Entry(root, textvar=entry_text, font=("Arial", 20), bd=8, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# Buttons erstellen
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", ".", "+",
    "="
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