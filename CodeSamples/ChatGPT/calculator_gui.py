import tkinter as tk
from tkinter import messagebox

def on_button_click(value):
    """Fügt den geklickten Button-Wert zur Eingabezeile hinzu."""
    if value == "=":
        try:
            result = eval(entry.get())  # Berechnet den eingegebenen Ausdruck
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Fehler", "Ungültige Eingabe")
    elif value == "C":
        entry.delete(0, tk.END)  # Löscht die Eingabezeile
    else:
        entry.insert(tk.END, value)  # Fügt den Wert zur Eingabezeile hinzu

# Hauptfenster erstellen
root = tk.Tk()
root.title("Taschenrechner")

# Eingabefeld erstellen
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Tasten definieren
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Tasten auf dem Fenster anordnen
row, col = 1, 0
for button in buttons:
    action = lambda x=button: on_button_click(x)
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14), command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:  # Nach vier Spalten eine neue Zeile beginnen
        col = 0
        row += 1

# Hauptschleife starten
root.mainloop()
