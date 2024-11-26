import tkinter as tk

def click(event):
    global entry_text
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry_text.get())
            entry_text.set(result)
        except Exception as e:
            entry_text.set("Error")
    elif text == "C":
        entry_text.set("")
    else:
        entry_text.set(entry_text.get() + text)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Taschenrechner")
root.geometry("600x400")

entry_text = tk.StringVar()
entry = tk.Entry(root, textvar=entry_text, font=("Arial", 20), bd=8, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

# Button-Layout
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Buttons erstellen
row = 0
col = 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font=("Arial", 18), width=5, height=2, relief=tk.RAISED)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()